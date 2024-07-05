from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def failed(score):
    exp={'score':score,'res':"failed"}
    return render_template('result.html',result =exp)

@app.route('/passed/<int:score>')
def passed(score):
    exp={'score':score,'res':"Passed"}
    return render_template('result.html',result=exp)

@app.route('/submit',methods=['POST','GET'])
#this will be my result checker page
#how to read posted values
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['math'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+data_science)
    res=""
    if(total_score > 50):
        res="passed"
    else :
        res= "failed"   


    return redirect(url_for(res,score=total_score))


if __name__ == "__main__":
    app.run(debug=True)