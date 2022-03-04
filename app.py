from ast import If
from pickle import TRUE
from flask import Flask, request, render_template, url_for
import pickle

vector = pickle.load(open("vectorizer.pkl",'rb'))
model = pickle.load(open("finalized_model.pkl",'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')    
    
@app.route('/prediction',methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = request.form['news']
        print(news)
        predict = model.predict(vector.transform([news]))[0]
        print(predict)

        return render_template("prediction.html", prediction_text="news Result is->{}".format(predict))
    else:
       return render_template('prediction.html')    
    

if __name__ == '__main__':
    app.run(debug=True,port=8000)