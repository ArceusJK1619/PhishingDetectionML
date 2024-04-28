from flask import Flask, request, jsonify, render_template
from process import predict

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    prediction =""
    if request.method == "POST":
        url = str(request.form['url'])
        print(url)
        prediction = predict(url)
        #do proccess with url here.
        if len(prediction)>0:
            return render_template('index.html', prediction = prediction)
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)