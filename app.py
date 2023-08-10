import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

import stats
import preprocess

st.set_page_config(
    page_title="Whatsapp chat analyzer",
    page_icon="chart_with_upwards_trend",
)
css_example = '''
<img src="https://img.icons8.com/color/96/null/whatsapp--v1.png"/>'''
st.write(css_example, unsafe_allow_html=True)
st.title("WhatsApp chat analysis using python")
st.header("Analyze your whatsapp your chats easily !")

uploaded_file = st.file_uploader("Please select your .txt file... ")

want_help = '<a href = "https://faq.whatsapp.com/1180414079177245/?cms_platform=android"> How to save whats app ' \
            'chats? </a> '
st.caption(want_help, unsafe_allow_html=True)

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocess.process(data)

    # st.dataframe(df)

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
    selected_user = st.sidebar.selectbox("Show analysis with respect to", user_list)

    # footer
    space = ' <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/> ' \
            '<br/> <br/> <br/> <br/> <br/> <br/> <br/> <br/>'
    website = '<a href="https://gauravgarwa.vercel.app/" style="font-family:sans-serif; ' \
              'font-size: 14px; text-decoration: none;"> Gaurav Garwa </a> '
    st.sidebar.caption(space, unsafe_allow_html=True)
    st.sidebar.caption("Developed by " + website, unsafe_allow_html=True)
    st.sidebar.caption(
        "Connect with me on: " + " [Linkedin](https://www.linkedin.com/in/ggarwa/)" + " [Github](https://github.com/gaurav1832)"
        + " [Twitter](https://twitter.com/ggauravvvvv)" + " [Instagram](https://www.instagram.com/gauaurarav/)")

    if st.button("Analyze"):
        total_messages, total_words, total_media, links_list, total_links = stats.fetch_stats(selected_user, df)
        st.title("Statistics")
        c1, c2, c3 = st.columns(3)

        with c1:
            st.subheader("Total messages")
            st.title(total_messages)

        with c2:
            st.subheader("Total words")
            st.title(total_words)

        with c3:
            st.subheader("Media shared")
            st.title(total_media)

        # displaying the links shared

        st.subheader("Total number of links shared")
        c1, c2 = st.columns(2)
        with c1:
            st.title(total_links)
        for i in links_list:
            st.write(i)

        # finding the busiest person
        if selected_user == 'Overall':
            st.title("Most active user")
            x, new_df = stats.most_active(df)
            fig, ax = plt.subplots()

            c1, c2 = st.columns(2)

            with c1:
                ax.stem(x.index, x.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with c2:
                st.dataframe(new_df)

        # most common words
        st.title(selected_user + " most common words")
        common_df = stats.most_common_words(selected_user, df)

        fig, ax = plt.subplots()
        ax.barh(common_df[0], common_df[1])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Wordcloud
        st.title(selected_user + " wordcloud")
        df_wc = stats.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        plt.imshow(df_wc)
        st.pyplot(fig)

        # emoji stats
        # st.title(selected_user + " emoji stats")
        # emoji_df = stats.emoji_stats(selected_user, df)

        # c1, c2 = st.columns(2)
        #
        # with c1:
        #     st.dataframe(emoji_df)
        # # with c2:
        # #     st.subheader(selected_user + " Most used emojis")
        # #     fig, ax = plt.subplots()
        # #     ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct='%0.2f')
        # #     st.pyplot(fig)

        # monthly timeline
        st.title(selected_user + " monthly timeline")
        timeline = stats.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        st.title(selected_user + " daily timeline")
        daily_timeline = stats.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily activity map
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header(selected_user + " most busy day")
            busy_day = stats.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='pink')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header(selected_user + " most busy month")
            busy_month = stats.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title(selected_user + " weekly heatMap")
        user_heatmap = stats.heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)
