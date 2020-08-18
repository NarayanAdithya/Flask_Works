from flask import Flask, jsonify, render_template, request,url_for
from plot import create_plot
app = Flask(__name__)


@app.route('/_add_numbers',methods=['GET','POST'])
def add_numbers():


    return 'hey'

@app.route('/',methods=['GET','POST'])
def index():
    print("Posted")
    bar=None

    content=request.form.to_dict()
    print(content)
    bar=create_plot(content)
    return render_template('index.html',plot=bar)

if __name__ == '__main__':
    app.run(debug=True)
