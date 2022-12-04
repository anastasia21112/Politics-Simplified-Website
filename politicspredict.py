import mediacloud
import mediacloud.api, json, datetime
import mediacloud.tags
import csv
import pandas
import requests
from bs4 import BeautifulSoup
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords
import re
# nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

def all_matching_stories(mc_client, q, fq):
    """
    Return all the stories matching a query within Media Cloud. Page through the results automatically.
    :param mc_client: a `mediacloud.api.MediaCloud` object instantiated with your API key already
    :param q: your boolean query
    :param fq: your date range query
    :return: a list of media cloud story items
    """
    last_id = 0
    more_stories = True
    stories = []
    # while more_stories:
    page = mc_client.storyList(q, fq, last_processed_stories_id=last_id, rows=50, sort='processed_stories_id')
    print("  got one page with {} stories".format(len(page)))
    if len(page) == 0:
        more_stories = False
    else:
        stories += page
        last_id = page[-1]['processed_stories_id']
    return stories

my_query = "Joseph Ferreira AND Massachusetts"
def get_all_stories_file(mc_client, q, fq):
    all_stories = all_matching_stories(mc_client, q, fq)
    for s in all_stories:
        # see the "language" notebook for more details on themes
        theme_tag_names = ','.join([t['tag'] for t in s['story_tags'] if t['tag_sets_id'] == mediacloud.tags.TAG_SET_NYT_THEMES])
        s['themes'] = theme_tag_names
    # now write the CSV

    fieldnames = ['stories_id', 'publish_date', 'title', 'url', 'language', 'ap_syndicated', 'themes', 'media_id', 'media_name', 'media_url']
    with open('story-list.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        for s in all_stories:
            writer.writerow(s)
    story_df = pandas.read_csv('story-list.csv')
    return story_df
def get_words_from_all_websites(stories_file):
    urls = list(stories_file['url'])[-20:-1]
    urls_string = ""
    for url in urls:
        urls_string += url + ","
    print(urls_string)
    ultimate_string = ""
    for count, url in enumerate(urls):
        print("On the ", count, "URL.")
        print("The URL is, ", url)
        try:
            page = requests.get(url)
        except:
            continue
        soup = BeautifulSoup(page.content, "html.parser")
        python_paragraph = soup.find_all("p", string="")
        all_words = []
        for element in python_paragraph:
            all_words.append(' ' + element.get_text(' ', strip=True) + ' ')
        all_words_string = ''.join(all_words)
        text = all_words_string
        sentences = nltk.sent_tokenize(text)
        stop_words = set(stopwords.words("english"))
        words = []
        for sentence in sentences:
            res = re.sub(r'[^\w\s]', '', sentence)
            for word in nltk.word_tokenize(res):
                words.append(' ' + word + ' ')
        without_stop_words = [word for word in words if not word in stop_words]
        without_stop_words_string = ''.join(without_stop_words)
        ultimate_string += without_stop_words_string
    return ultimate_string, urls_string
def get_polarity_score(mc_client, q, fq):
    print("in this function")
    stories_file = get_all_stories_file(mc_client, q, fq)
    all_words, urls_string = get_words_from_all_websites(stories_file)
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(all_words)
    return score, urls_string
# mc = mediacloud.api.MediaCloud('d6c3a5b68985d91494c3e253f1378bbbb098259d7668ddadc42146b7bbc9ca4e')
# my_query = "Joseph Ferreira AND Massachusetts"
# start_date = datetime.date(2022,10,4)
# end_date = datetime.date(2022,11,4)
# date_range = mc.dates_as_query_clause(start_date, end_date)
# # story_file = get_all_stories_file(mc, my_query, date_range)
# print(get_polarity_score(mc, my_query, date_range))