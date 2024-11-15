from flask import Flask, request, jsonify  
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    return 'HELLO'

@app.route('/hi/')       
def Hi(): 
    return 'Hi  tHis is hi'

# GET method --> collect data from url and pass back data to server in json.
@app.route('/get-user/<userId>/')       
def get_user(userId): 
    user_data = {
        "user_id":userId,
        "Name":"John wick",
        "Profession":"killing..."
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200

# POST method --> Based on method call will gather data from the HTML and parse it into json and store to DB
@app.route('/create-user/',methods = ["POST"])       
def create_user():
    if request.method == "POST":
        data = request.get_json()

        return jsonify(data)

if __name__=='__main__': 
   app.run() 
