from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route("/")
def root():
    return f"This is the root."

@app.route('/hello/<name>')          # The "@" decorator associates this route with the function immediately following
def hello(name):
    return f"Hello {name}"  # Return the string 'Hello World!' as a response

@app.route("/users/<username>/<id>")
def show_user_profile(username, id):
    print(username)
    print(id)
    return f"username: {username}, id: {id}"

@app.route("/success")
def seccess():
    return "success"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  