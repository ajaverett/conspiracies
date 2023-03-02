"""
Instruction page.
"""

import streamlit as st

st.title('Instructions')
st.markdown("""---""")


with st.container():

    st.header('How to use this Streamlit app')

    st.write('''
    This Streamlit page is a data analysis tool that allows users to explore and visualize public forum data related to conspiracy theories. The tool loads in a dataset of Reddit posts that mention a specific query, which can be selected based on different genres such as governmental, corporate, scientific, and other.

    The user can filter down the subreddits they want to analyze using checkboxes for r/Politics, r/PoliticalDiscussion, r/conspiracy, and r/Freethought. They can also input a secondary query to see how often it appears in the posts related to the initial query. 
    
    The data is then cleaned and processed. The tool then visualizes the popularity of the initial query over time on Reddit, using a line chart that shows the number of posts mentioning the query each month. The chart distinguishes between posts that include the secondary query and those that do not.

    Finally, the chart is displayed on the Streamlit page, with the option to adjust the chart's width. Users can hover over the chart to see the number of posts for each month, and they can use the legend to toggle between mentions of the initial query and mentions of both the initial and secondary queries.
    ''')

    st.header('What is Reddit?')
    
    st.markdown("Reddit is a social media site with various\
        forums called subreddits. Our site collects data from four subreddits specificially: Conspiracy, Politics,\
            PoliticalDiscussion, and Freethought. To collect this data, we use Reddit's builtin API.")
    
    st.header('What is Plotly?')

    st.write("Plotly is a data visualization tool that allows us to create interactive graphs. We use Plotly to create our graphs, and we use Streamlit to display them on our site.")

    st.markdown('''
    To use this interactive graph outlining trends on conspiracies, it is a very simple \
    process. First, select the topic you would like to see trends on. Then, select the query from the selected topic\
    that you would like to see trends on. Then, select the subreddits you want to include. You can then type in a\
    second query to see how it matches up with the first query.\
                Lastly, you can mess with various settings on the graph, including:
                
                ''')

    st.markdown('- Downloading graph as a PNG')
    st.markdown('- Zooming in and out')
    st.markdown('- Panning across graph')
    st.markdown('- Autoscaling graph')
    st.markdown('- Resetting the axes')
    st.markdown('- Viewing graph in fullscreen mode')

    st.markdown('Once you figure everything out, you will be a master at using our site.')
    st.markdown('Enjoy!')
