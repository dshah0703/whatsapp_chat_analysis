# WhatsApp Chat Analyzer

## Overview

WhatsApp Chat Analyzer, gives an overview of the activities of users and messages shared between individuals as well as in a group. It identifies the sentiment of a WhatsApp group and each user.

## Deployed on Heroku

This deployed web app is live at - [https://whatsapp-chat-analyzer-deva.herokuapp.com/](https://whatsapp-chat-analyzer-deva.herokuapp.com/) .

## Features 

1.	Provides option to upload chat exported from WhatsApp
2.	Shows analysis with respect to overall group and on individual basis
3.	 Provides top statistics regarding Messages, Words, Media/ Links shared
4.	Identifies Sentiment of Overall WhatsApp chat and individual user – Positive/Negative/Neutral
5.	Shows graphical visualization regarding activities of a user with the help of WordCloud, Heatmap and Line/Bar Graph


### The web app was built on python using the following libraries:

* streamlit
* pandas
* numpy
* Matplotlib
* Seaborn
* Urlextract
* Wordcloud
* nltk

## File Structure

1. `preprocess.py` = Performed data cleaning and preprocessing of WhatsApp texts 
2. `helper.py` = Consist functions that helps to generate graphs and sentiment analysis to show on Website
3. `app.py` = Used Steamlit to run and display all analysis of WhatsApp chat.
4. `whatsapp_chat_analysis.ipynb` = Peformed data exploration and analysis to select visualizations and build webapp
5. `requirements.txt` = Package installation requirements to run *stramlit-app.py* file on server.
6. `Procfile` = Commands to execute that run webapp on server
7. `setup.sh` = Server side configuration

## Run file
steamlit run app.py

## Screenshots

![App Screenshot](https://user-images.githubusercontent.com/77790306/186555185-25d1d40b-42dd-4185-b51e-8ed39644bd5e.jpeg)

![App Screenshot](https://user-images.githubusercontent.com/77790306/186555271-d5a78e6f-a904-4532-af2c-2f5168d0c6ad.jpeg)






