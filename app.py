import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
st.sidebar.title("Whatsapp Chat Analyzer 🤹‍")

uploaded_file = st.sidebar.file_uploader("Choose a file 📂")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)


    #fetch Unique users
    user_list = df['user'].unique().tolist()
    user_list.remove("group_notifications")
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show Analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):

        num_messages,words, num_media_messages,num_links = helper.fetch_stats(selected_user,df)

        new_title = '<h1 style="font-family:sans-serif; color:Purple;">Top Statistics 📊📈 </h1>'
        st.markdown(new_title, unsafe_allow_html=True)

        st.write("""
                               --- 
                               """)
        col1,col2,col3,col4 = st.columns(4)

        with col1:
            new_title = '<h4 style="font-family:sans-serif; color:darkblue;"> Total Messages 📩 </h4>'
            st.markdown(new_title, unsafe_allow_html=True)
            st.title(num_messages)

        with col2:
            new_title = '<h4 style="font-family:sans-serif; color:darkblue;"> Total Words 🗣️ </h4>'
            st.markdown(new_title, unsafe_allow_html=True)
            st.title(words)

        with col3:

            new_title = '<h4 style="font-family:sans-serif; color:darkblue;"> Media Shared 🖼️ </h4>'
            st.markdown(new_title, unsafe_allow_html=True)
            st.title(num_media_messages)

        with col4:
            new_title = '<h4 style="font-family:sans-serif; color:darkblue;"> Links Shared 🔗 </h4>'
            st.markdown(new_title, unsafe_allow_html=True)
            st.title(num_links)
        st.write("""
        --- 
        """)

        # sentiment_analysis

        new_title = '<h2 style="font-family:sans-serif; color:Green;"> Sentiment Analysis 😊😑☹️ </h2>'
        st.markdown(new_title, unsafe_allow_html=True)
        sentiment_df = helper.sentiment_analysis(selected_user, df)



        if sentiment_df == 'Positive':
            st.subheader(f'Sentiment of {selected_user}: Positive 😊')
        elif sentiment_df == 'Neutral':
            st.subheader(f'Sentiment of {selected_user}: Neutral 😑')
        else:
            st.subheader(f'Sentiment of {selected_user}: Negative ☹')



        st.write("""
                --- 
                """)

        #Monthly timeline

        new_title = '<h2 style="font-family:sans-serif; color:Green;"> Monthly Timeline</h2>'
        st.markdown(new_title, unsafe_allow_html=True)
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'],color = 'darkblue')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #Daily Timeline
        new_title = '<h2 style="font-family:sans-serif; color:green;"> Daily Timeline</h2>'
        st.markdown(new_title, unsafe_allow_html=True)

        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.write("""
                       --- 
                       """)

        #Activity Map
        new_title = '<h2 style="font-family:sans-serif; color:green;"> Activity Map</h2>'
        st.markdown(new_title, unsafe_allow_html=True)
        col1,col2 = st.columns(2)

        with col1:
            st.subheader("Most Active Day 📅")
            busy_day = helper.week_activity_map(selected_user,df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            plt.xticks(rotation='vertical')

            st.pyplot(fig)

        with col2:
            st.subheader("Most Active Month 📆")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color = 'orange')
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)

        st.write("""
                     --- 
                        """)

        new_title = '<h2 style="font-family:sans-serif; color:green;">Weekly Activity Map 📈</h2>'
        st.markdown(new_title, unsafe_allow_html=True)
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        st.write("""
                       --- 
                       """)


        # finding the busiest users in the group
        if selected_user == 'Overall':
            new_title = '<h2 style="font-family:sans-serif; color:green;">Most Active User 📱</h2>'
            st.markdown(new_title, unsafe_allow_html=True)
            x, new_df= helper.most_busy_user(df)
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color = (0.5,0.1,0.5,0.6))
                plt.xticks(rotation = 'vertical')
                plt.ylabel('Messages')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        # WordCloud
        new_title = '<h2 style="font-family:sans-serif; color:green;">WordCloud</h2>'
        st.markdown(new_title, unsafe_allow_html=True)
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)


        st.write("""
                       --- 
                       """)


        #most common words
        most_common_df = helper.most_common_words(selected_user,df)

        fig, ax = plt.subplots()

        ax.barh(most_common_df[0],most_common_df[1], color = 'purple')
        plt.xticks(rotation = 'vertical')

        new_title = '<h2 style="font-family:sans-serif; color:green;">Most Common Words</h2>'
        st.markdown(new_title, unsafe_allow_html=True)
        plt.ylabel('Words')
        plt.xlabel('Frequency')
        st.pyplot(fig)








