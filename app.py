from flask import Flask, render_template, request
import openai
import os 
from dotenv import load_dotenv,find_dotenv

__ = load_dotenv(find_dotenv()) #read local .env file
openai.api_key=os.environ["OPENAI_API_KEY"]

app = Flask(__name__)
app.static_folder = 'static'
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    
    userText = request.args.get('msg')
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": userText}
    ]
    )
    result=completion.choices[0].message['content']
 
    return result
   


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8002,debug=True)
