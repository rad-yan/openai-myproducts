from flask import Flask, render_template, url_for, redirect, request, send_file, jsonify
from flask_cors import CORS
import openai
import os

# packages -- pip install flask flask-cors 
# -- pip install openai==0.27.0
# export OPENAI_API_KEY="sk-apikey1234"




openai.api_key = os.getenv("OPENAI_API_KEY")# we will use it once it is deployed 

app = Flask(__name__)
CORS(app) # Enable CORS


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/theone')
def theone():
    return render_template('theone.html')


@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.get_json()
    system = data.get('system')
    conversation = data.get('conversation', [])

    # Call GPT-3 API here with system and user parameters
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": system}] + conversation
        )
        assistant_response = response['choices'][0]['message']['content']
        print(response)
    except Exception as e:
        print(f"Error: {e}")  # Print the error message
        assistant_response = "Hold on there! We can't keep everything forever. To make way for the new, we'll have to let go of the past. So, we're starting anew but don't worry your next prompt will write history again."  # Define the variable before returning it
    return jsonify({"assistant": assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
