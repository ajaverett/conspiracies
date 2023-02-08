import streamlit as st

st.title('Instructions')


with st.container():
    
    
    st.markdown("This site uses Reddit to gather all of the data. Reddit is a social media site with various\
        forums called subreddits. Our site collects data from four subreddits specificially: Conspiracy, Politics,\
            PoliticalDiscussion, and Freethought. To collect this data, we use Reddit's builtin API.")
    st.markdown('''
    To use this interactive graph outlining trends on conspiracies, it is a very simple \
    process. First, select the initial query that you would like to see trends on. Then, select the subreddits\
            you want to include. You can then type in a second query to see how it matches up with the first query.\
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