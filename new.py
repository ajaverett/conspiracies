"""
To create csv files of subreddits you want to 
"""

"""
List of 3-4 queries of each of our conspiracy topics: 
Science/Tech
- younger dryas cataclysm
- global warming
- climate change

Political
- fraud
- hoax
- ukraine
- russia

Medicine
- spike proteins
- big pharma
- phizer
- moderna
- autism
- vaccine
- transgender
- puberty blockers

Business/Economic
- chemtrail



List more features for the streamlit app:
---
"""

import praw
import pandas as pd

CLIENT_ID = 'Hu7d3YxgUE8Q2qzAZ-4KAQ'
CLIENT_SECRET = 'n_ob1N4v83hR7F1r_VEhl4mLU2KlTw'
USER_AGENT = 'ConspiracyWebScrape'

# Acessing the reddit api
reddit = praw.Reddit(client_id=CLIENT_ID, # your client id
client_secret=CLIENT_SECRET,  # your client secret
user_agent=USER_AGENT)  # your user agent


csv_df = pd.DataFrame({
            "title" : [],
            "score" : [],
            "id" : [],
            "url" : [],
            "comms_num": [],
            "created" : [],
            "body" : [],
            "subreddit" : [],
            "query":[]
        })

sub = ['conspiracy','PoliticalDiscussion','politics','geopolitics','Freethought']  # make a list of subreddits you want to scrape the data from
# r\conspiracytheories

#  obama 'big pharma' 'Alex jones' 'Vaccine' 'Ukraine' 'Transgender' 'Soros' 'Russia' '5G' 'Soy' 'Musk' 'QAnon' 'plandemic' 'climate change' 'microchip' 'Zodiac' 'CIA' 'Biden' 'NSA' 'Chemtrail'
query = ['Chemtrail']
# query = ['Fauci']

for s in sub:
    subreddit = reddit.subreddit(s)   # Chosing the subreddit

    for item in query:
        post_dict = {
            "title" : [],
            "score" : [],
            "id" : [],
            "url" : [],
            "comms_num": [],
            "created" : [],
            "body" : [],
            "subreddit" : [],
            "query":[]
        }

        for submission in subreddit.search(query,sort = "top",limit = 100000):
            post_dict["title"].append(submission.title)
            post_dict["score"].append(submission.score)
            post_dict["id"].append(submission.id)
            post_dict["url"].append(submission.url)
            post_dict["comms_num"].append(submission.num_comments)
            post_dict["created"].append(submission.created)
            post_dict["body"].append(submission.selftext)
            post_dict['subreddit'].append(s)
            post_dict['query'].append(item)
        
        post_data = pd.DataFrame(post_dict)
        csv_df= pd.concat([csv_df,post_data])
 

csv_df.to_csv(f"{query[0]}_reddit.csv")