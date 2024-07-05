from flask import Flask,redirect,url_for

app =Flask(__name__)

@app.route('/')
def welcome():
    return "Konichiwa"

@app.route('/success/<int:score>')
def success(score):
    return f"The person has passed ans the mrks is {score}"

@app.route('/fail/<int:score>')
def fail(score):
    return f"The person has failed ans the mrks is {score}"

@app.route('/score/<int:score>')
def results(score):
    if score >50:
        return redirect(url_for('success',score=score))
    else:
        return redirect(url_for('fail',score=score))

if __name__ =='__main__':
    app.run(debug=True)

