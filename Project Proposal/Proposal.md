# AIM Labs Project Overview
## Politics Simplified
**Contributors:** Anastasia, Quincy, Anika

**Date:** October 14, 2022

### Description
The world of politics can be overwhelming for most. With so many different sources to learn from, biases in the media, and countless candidates, voters are at a loss of who to cast their vote for when local elections pop up. However, in this day and age, it is vital that everyone who has the ability to, exercises their right to vote. To increase voter turnout and make voters more informed, we propose a website that simplifies the candidate research process by taking in the county of the voter and providing a range of different potential candidates along with their political profiles.

Our project will focus on creating a website that analyzes news articles, social media platforms, and other digital repositories of various political candidates to create a comprehensive summary of their political career and most recent platform. Users will input the Massachusetts county they are interested in, and the website will output the political candidates in that area with the profiles created from the aforementioned data analysis. Optionally, users can take a quiz to match them with a political candidate that best matches their political and socio economic beliefs. As mentioned before, the scope of the project will be limited to the state of Massachusetts.

### Description Components
* Homescreen
  
When the user first clicks onto the website, the user will be taken to the welcome screen that welcomes them to the site along with a quick tagline of what the website does. It will prompt the user to enter information about their Massachusetts country. 

![alt text]("./assets/Politics Simplified Wireframes-01.png" "Title")

* About (Politics)

There will be a page with a general description of how the political structure of Massachusetts works and how our project fits into that. It will also have general information about politics. 

* About (Project)
  
This general about page will serve as a way for users to understand what our model does. We will be transparent about where the data comes from, the algorithm used, and how we created the political platforms. 

* Results

This is where the different political candidates are presented based on what the user enters for their county. There will be different cards for each candidate that the user can click through. 

* Profile Card

Contain top news sources the candidate has been mentioned in, top ideas that they talk about, a graph of 10 years of how much the candidate has been in the news. 

* Quiz
  
A quiz that takes in information about the voter’s beliefs and tries to match the voter with a candidate in their area that has views similar to them. 

* Model

### Datasets and Models

* News Sources
  * [Media Cloud](https://mediacloud.org/)
  * Explorer
  * Topic Mapper
* [Candidates](https://www.sec.state.ma.us/ele/ele22/state_election_candidates22.htm)
* Twitter API
* Meta for Developers

### Expectations for Challenges
* While designing the project, we realized that trying to get data on every candidate in the US who is running for local office is very challenging, so we had to evolve our project to be more doable by only focusing on Massachusetts. The extensibility of this project relies on data that is accessible. While it is possible to get data on local candidates of a certain region, it is hard to get data on candidates from many regions. 
* It will be hard to “infer” political ideas from candidates based on news sources. This may require skills beyond Natural Language Processing, but we have decided to still attempt crafting a political platform for each candidate. The political platform format can evolve in the future, and it may just be a combination of different taglines and news sources they’re in, but we will decide that later in the project while we still think creating a comprehensive political platform is possible. 
* By using many different types of data (textual, numerical, etc.), it will be hard to format all the data into a consistent, usable form for our model to use. We will need to compile all the data into a single dataset and decide how to represent each feature. 
* The ethics of matching up someone with a candidate who is best for them is something to consider. With easily influential voters, it may be questionable to introduce a tool that steers them into a certain direction of who to vote for. Although it is based on data, the model itself could have biases towards certain features that don’t hold relevance to political aptitude or similarity to a voter.

## Calendar

### Week 1 (Due October 15)
For week 1, we will have the project proposal done and an agreed on conceptual understanding of the project. 
| Person| Progress and Personal Deliverable | Est. Time
|------|------|------|
| Quincy | Overview, Component Diagrams, Backend algorithmic pondering| 150 minutes
| Anika | Description of Components, Models/Datasets (Counties - Political Candidates), Diagram for Mass. Political Candidates| 120 minutes
| Anastasia | Challenges, Description of Components. Create a git repository for the markdown file, and start typing up the information. | 90 minutes

### Week 2 (Due October 22)
For week 2, we will have the database set up and the basic frontend/backend of the website done. 
| Person| Progress and Personal Deliverable | Est. Time
|------|------|------|
| Quincy | Work on setting up basic website with Anastasia| 180 minutes
| Anika | Database set up| 180 minutes
| Anastasia | Work on setting up basic website w Quincy (create Github repository) | 180 minutes

### Week 3 (Due October 29)
For week 3, we want to have the web scraper set up, and API/database familiarity. 
| Person| Progress and Personal Deliverable | Est. Time
|------|------|------|
| Quincy | Work on web scraper- a tool that translates articles and web data into data we can preprocess and use for our NLP classification models. | 300 minutes
| Anika | Investigate how to use different API’s and the mediacloud dataset, get familiar. Acquire API necessary API keys. Create a guide for other members to quickly learn essentials.| 300 minutes
| Anastasia | Work on web scraper- a tool that translates articles and web data into data we can preprocess and use for our NLP classification models.  | 300 minutes

### Week 4 (Due November 5)
For week 4, we want to be done with creation of the classification algorithm including training and testing. 
| Person| Progress and Personal Deliverable | Est. Time
|------|------|------|
| Quincy | Aid in implementation and training of the algorithm on a subset of data (current political candidates). | 300 minutes
| Anika | Aid in implementation of the algorithm. Integrate APIs into the website and load datasets into the database.| 300 minutes
| Anastasia | Work on preprocessing of data. Aid in implementation of the NLP classification algorithm. | 240 minutes

### Week 5 (Due November 19)
For week 5, we will be done with the evaluation of the algorithm. 
| Person| Progress and Personal Deliverable | Est. Time
|------|------|------|
| Quincy | Evaluate the NLP algorithm on the subset of data not used in training (past political candidates). Adjust and train the algorithm further based on the results of the evaluation.| 300 minutes
| Anika | Work on user quizzes for the website and UI/UX for candidate search and summary pages.| 300 minutes
| Anastasia | Reach out to the 17.50 professor for feedback on the political candidate summaries and classification and project in general. Implement feedback. Help Anika with the website.| 240 minutes

### Week 6 (Due December 3)
For week 6, we will work on deployment and testing and final integration of the model into the website. 

| Person| Progress and Personal Deliverable | Est. Time
|------|------|------|
| Quincy | Integrating all components, evaluating UX and component interaction via end-to-end testing. If there is enough time, work on final demo day slides| 300 minutes
| Anika | Integrating all components, evaluating UX and component interaction via end-to-end testing. If there is enough time, work on final demo day slides| 300 minutes
| Anastasia | Integrating all components, evaluating UX and component interaction via end-to-end testing. If there is enough time, work on final demo day slides| 300 minutes

### Week 7 (Due December 10)
For week 7, we will be done with the model and integration. We will focus on practicing our final presentation for demo day. 
| Person| Progress and Personal Deliverable | Est. Time
|------|------|------|
| Quincy | Work on final demo day slides, practice final presentation, and perfect slides| 180 minutes
| Anika | Work on final demo day slides, practice final presentation, and perfect slides| 180 minutes
| Anastasia | Work on final demo day slides, practice final presentation, and perfect slides| 180 minutes

