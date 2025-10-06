from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import json
import pickle

# Load pre-trained model and artifacts
model = tf.keras.models.load_model('models/career_chatbot_model.h5')

with open('models/tokenizer.pickle', 'rb') as f:
    tokenizer = pickle.load(f)

with open('models/label_encoder.pickle', 'rb') as f:
    label_encoder = pickle.load(f)

with open('response_templates.json', 'r') as f:
    responses = json.load(f)

app = Flask(__name__)

# Helper function to predict intent and get response
def get_bot_response(user_input):
    seq = tokenizer.texts_to_sequences([user_input])
    padded = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=50, padding='post')
    pred = model.predict(padded)
    intent = label_encoder.inverse_transform([np.argmax(pred)])[0]
    return np.random.choice(responses[intent])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chat():
    user_msg = request.form['msg']
    bot_response = get_bot_response(user_msg)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
