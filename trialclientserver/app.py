from flask import Flask,url_for,redirect,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        print("Posting data")
        for input in request.form:
            row = request.form[input].split(";")
            print("--------------------------")
            print("Name: " + row[0]);
            print("Job: " + row[1]);
            print("Country " + row[2]);
    return render_template('index.html',title='Index')





if __name__ == '__main__':
    app.run(debug=True)
