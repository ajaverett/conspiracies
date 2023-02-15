import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import re


beginning = st.container()
query_section = st.container()
viz_section = st.container()
subreddit = st.container()

with beginning:
    st.title('Analyzing conspiracies through public forum data')

with query_section:

    genre = st.radio("",("Governmental", "Corporate", "Locations", "Scientific","Other"))

    if genre == 'Governmental':
        query = st.selectbox('Initial Query',('CIA','NSA','Clinton','Fauci','Obama','Trump','QAnon'))
    elif genre == 'Corporate':
        query = st.selectbox('Initial Query',('Epstein','Bill Gates','Harvey Weinstein','Musk','Podesta','Soros'))
    elif genre == 'Locations':
        query = st.selectbox('Initial Query',('Russia','Ukraine','Wuhan','Wyoming'))
    elif genre == 'Scientific':
        query = st.selectbox('Initial Query',('5G','big pharma','Chemtrail','climate change','microchip','plandemic','Vaccine'))
    elif genre == 'Other':
        query = st.selectbox('Initial Query',('Alex Jones','fraud','hoax','soy','Transgender','Zodiac'))

    query_display = (np.where(bool(re.search(r'\d', query)),query,np.where(query.isupper(), query, query.capitalize())))
          
    beginning.header(f':blue[Query: {query_display}]')

    second_query = st.text_input("Secondary Query")

    #Load in Data
    df = pd.read_csv(f"data/{query}_reddit.csv")

with viz_section:
    st.text("")

with subreddit:
    st.write('Filter down subreddits')
    option_1 = st.checkbox('r/Politics')
    option_2 = st.checkbox('r/PoliticalDiscussion')
    option_3 = st.checkbox('r/conspiracy')
    option_4 = st.checkbox('r/Freethought')

    filters = []

    if option_1: filters.append('politics')
    elif option_2: filters.append('PoliticalDiscussion')
    elif option_3: filters.append('conspiracy')
    elif option_4: filters.append('Freethought')

    # Apply filters to dataframe
    if filters:
        df = df.query("subreddit in @filters")

    
    # Make a column to see if the second query is in the df
    df = (df
        .fillna('n/a')
        .assign(body = lambda x: x.body.str.lower(),
                title = lambda x: x.title.str.lower())
        .assign(
            has_conspiracy = lambda x:
                np.where(
                    x.body.str.contains(second_query.lower(), na = False), True,
                np.where(
                    x.title.str.contains(second_query.lower(), na = False), True,
                    False)))   
    )

    #Tidyer Dates
    df = (df
        .assign(created = lambda x: pd.to_datetime(x['created'], unit='s'))
        .assign(created = lambda x: x['created'].dt.to_period('M').dt.to_timestamp())
    )

    df_grouped = df.groupby(by=['created','has_conspiracy'], as_index= False).count().dropna()

    fig = px.line(
        df_grouped, 
        x="created", 
        y="id", 
        color="has_conspiracy", 
        title=f"Popularity of {query} over time on Reddit",
        )
    
    fig.update_layout(legend=dict(
        title="", 
        yanchor="top", 
        y=1.14,
        xanchor="left", 
        x=.00))
    fig.update_traces(line=dict(color='purple'), selector=0)
    fig.update_layout(xaxis_title="", yaxis_title="Number of posts by month", xaxis_tickformat='%b-%Y')


    if (len(df.query("has_conspiracy == True")) == 0):
        newnames = {'False':f'Mentions of {query}'}
        fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                            legendgroup = newnames[t.name],
                                            hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                            )
                        )   

    elif (second_query == ''):
        newnames = {'True':f'Mentions of {query}'}
        fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                            legendgroup = newnames[t.name],
                                            hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                            )
                        )    
    
    elif (len(df.query("has_conspiracy == False")) == 0):
        newnames = {'True':f"Mentions of {query} and '{second_query}'"}
        fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                            legendgroup = newnames[t.name],
                                            hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                            )
                        )    

    else:    
        fig.update_traces(line=dict(color='orange'), selector=1)
        newnames = {
            'True':f"Mentions of {query} and '{second_query}'", 
            'False':f'Mentions of Just {query}'}
        fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                            legendgroup = newnames[t.name],
                                            hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                            )
                        )

    viz_section.plotly_chart(fig, use_container_width=True)
