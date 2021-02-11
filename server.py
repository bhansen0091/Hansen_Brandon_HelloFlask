from flask import Flask, render_template
app = Flask(__name__)    

@app.route("/")
def index():
    return render_template("index.html", phrase="hello", times = 5)

@app.route('/hello/<name>')          
def hello(name):
    return f"Hello {name}"  

@app.route("/users/<username>/<id>")
def show_user_profile(username, id):
    print(username)
    print(id)
    return f"username: {username}, id: {id}"

@app.route("/success")
def seccess():
    return "success"

if __name__=="__main__":   
    app.run(debug=True)  