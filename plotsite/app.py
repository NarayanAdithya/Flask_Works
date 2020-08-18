from flask import Flask,render_template,url_for,request,jsonify
from plot import create_plot
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',title='Homepage')

# @app.route('/firstplot',methods=['GET','POST'])
# def plot():
#     bar=create_plot()
#     if request.method=='POST':
#          print("Posting data")
#          for input in request.form:
#             row = request.form[input].split(";")
#             print("--------------------------")
#             print("Task: " + row[0]);
#             print("Start Date: " + row[1]);
#             print("EndDate" + row[2]);
#     return render_template('firstplot.html',title='Plot',plot=bar)
@app.route('/ajaxtrial')
def ajaxtrial():
    a=requests.args.get('a',0,type=int)
    return jsonify(result=a**2)

@app.route('/squared')
def squared():
    return render_template('square.html',title='Square')





if __name__ == '__main__':
    app.run(debug=True)
