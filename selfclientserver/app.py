from flask import Flask, jsonify, render_template, request,url_for
from plot import create_plot
app = Flask(__name__)


@app.route('/_add_numbers',methods=['GET','POST'])
def add_numbers():


    return 'hey'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        print("Posted")
        bar=None
        content_title="NEW SAMPLE PLOT"
        content=request.form.to_dict()
        print(content)
        bar=create_plot(content)
        return render_template('index.html',plot=bar,comment='This is your gantt chart:')
    else:
        return render_template('index.html',plot=None,comment='Your chart will appear here:')

if __name__ == '__main__':
    app.run(debug=True)
