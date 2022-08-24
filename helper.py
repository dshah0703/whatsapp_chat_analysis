from urlextract import URLExtract
from collections import Counter
import pandas as pd
from wordcloud import WordCloud
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
#import emoji
extract = URLExtract()

def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch number of messages
    num_messages = df.shape[0]

    #fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    #fetch number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    #fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    return num_messages,len(words), num_media_messages, len(links)

# most busy user
def most_busy_user(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percentage'})
    return x, df

def create_wordcloud(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notifications']
    temp = temp[df['message'] != '<Media omitted>\n']  # remove media omitted

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            words.append(word)

    wc = WordCloud(width=500,height = 500,min_font_size=10, background_color= 'black',)
    df_wc = wc.generate(df['message'].str.cat(sep = " "))
    return df_wc

def most_common_words(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notifications']
    temp = temp[df['message'] != '<Media omitted>\n']  # remove media omitted

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

'''def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df'''

def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline

def week_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap

def sentiment_analysis(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]




    sent = SentimentIntensityAnalyzer()
    df['scores'] = df['message'].apply(lambda message: sent.polarity_scores(message))
    df['compound'] = df['scores'].apply(lambda score_dict: score_dict['compound'])
    df['sentiment_type'] = ''
    df.loc[df.compound > 0, 'sentiment_type'] = 'Positive'
    df.loc[df.compound == 0, 'sentiment_type'] = 'Neutral'
    df.loc[df.compound < 0, 'sentiment_type'] = 'Negative'

    result = df['sentiment_type'].value_counts().index[0]
    return result





