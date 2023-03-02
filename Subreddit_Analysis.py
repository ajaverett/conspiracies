# Linda's run command
# streamlit run C:\Users\Linda\OneDrive\Desktop\BYU-I_Computer_Science_Major\conspiracies\Subreddit_Analysis.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

container = st.container()

# with container:
#     st.sidebar.title('Instructions')

with st.container():
    st.title('Analyzing conspiracies through public forum data')

    query = st.selectbox(
    'Initial Query',
    ('Podesta', 'Harvey Weinstein','Epstein','Fauci','Wuhan'))

    container.header(f':blue[Query: {query}]')

    #Load in Data
    df = pd.read_csv(f"data/{query}_reddit.csv")
    st.text("")
    st.text("")



    st.write('Select Subreddits to include:')
    option_1 = st.checkbox('r/Politics')
    option_2 = st.checkbox('r/PoliticalDiscussion')
    option_3 = st.checkbox('r/conspiracy')
    option_4 = st.checkbox('r/Freethought')

    filters = []

    if option_1:
        filters.append('politics')
    if option_2:
        filters.append('PoliticalDiscussion')
    if option_3:
        filters.append('conspiracy')
    if option_4:
        filters.append('Freethought')


    # Apply filters to dataframe
    if filters:
        df = df.query("subreddit in @filters")

    st.text("")
    st.text("")


    second_query = st.text_input("Secondary Query")


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

    st.plotly_chart(fig, use_container_width=True)






    # John Podesta
    # Rothschilds
    # Flat Earth

