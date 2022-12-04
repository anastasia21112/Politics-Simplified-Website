from flask import Flask, make_response, render_template, request
from flask_navigation import Navigation
from politicspredict import get_polarity_score
import mediacloud
import mediacloud.api, json, datetime
import mediacloud.tags
app = Flask(__name__, template_folder='./templates')

nav = Navigation(app)
nav.init_app(app)

nav.Bar('top', [
    nav.Item('Home', 'home'),
    nav.Item('About', 'team'),
    nav.Item('Predict', 'sentiment')
])

# @app.route('/')
# def navpage():
#     return render_template('navpage.html')

# @app.route("/")
# def index():
#     return render_template('index.html')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/team.html")
def team():
    return render_template('team.html')
@app.route("/sentiment.html")
def sentiment():
    return render_template('sentiment.html')

# @app.route("/predict.html", methods=["POST"])
@app.route('/predict',methods = ['POST', 'GET'])
def predict():
    to_predict_list = request.form.to_dict()
    print("to_predict_list", request.form)
    review_text = to_predict_list['review_text']
    review_text.lstrip()
    review_text.rstrip()
    print("review text", review_text)
    mc = mediacloud.api.MediaCloud('d6c3a5b68985d91494c3e253f1378bbbb098259d7668ddadc42146b7bbc9ca4e')
    start_date = datetime.date(2022,10,4)
    end_date = datetime.date(2022,11,4)
    date_range = mc.dates_as_query_clause(start_date, end_date)
    sentiment_score, urls_returned = get_polarity_score(mc, review_text, date_range)

    # sentiment_score = get_score(sentiment_pipeline(review_text)[0])
    
    return render_template('predict.html', text = review_text, prediction = sentiment_score, urls = urls_returned)

    # sentiment_score = "NA"
    # # if request.method == 'POST':    
    # my_query = request.form['nm']
    # mc = mediacloud.api.MediaCloud('d6c3a5b68985d91494c3e253f1378bbbb098259d7668ddadc42146b7bbc9ca4e')
    # start_date = datetime.date(2022,10,4)
    # end_date = datetime.date(2022,11,4)
    # date_range = mc.dates_as_query_clause(start_date, end_date)
    
    # sentiment_score = get_polarity_score(mc, my_query, date_range)
    # return render_template('predict.html', prediction = sentiment_score)
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))
# def predict():
#     mc = mediacloud.api.MediaCloud('d6c3a5b68985d91494c3e253f1378bbbb098259d7668ddadc42146b7bbc9ca4e')
#     start_date = datetime.date(2022,10,4)
#     end_date = datetime.date(2022,11,4)
#     date_range = mc.dates_as_query_clause(start_date, end_date)
#     to_predict_list = request.form.to_dict()
#     my_query = to_predict_list['review_text']
    
#     sentiment_score = get_polarity_score(mc, my_query, date_range)
    
    # return render_template('predict.html', text = my_query, prediction = sentiment_score)
if __name__ == '__main__':
	app.run(host='localhost', port=50000, debug=True)