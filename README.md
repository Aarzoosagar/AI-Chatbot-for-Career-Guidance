# AI-Chatbot-for-Career-Guidance
Developed an AI-powered conversational chatbot designed to assist students and professionals in making informed career decisions. The chatbot interacts with users to understand their interests, academic background, and skills, then recommends suitable career paths, courses, and upskilling resources using natural language processing (NLP).

# 🎓 AI Chatbot for Career Guidance

An intelligent chatbot built using **TensorFlow** and **Natural Language Processing (NLP)** to provide personalized career and internship guidance.

## 🧩 Tech Stack
- **Languages:** Python  
- **Frameworks:** TensorFlow, Flask  
- **Libraries:** NLTK, Scikit-learn, NumPy, Pandas  
- **Concepts:** Intent Classification, Response Generation, Word Embeddings

## ⚙️ Features
- Predicts **user intent** (e.g., “career advice”, “internship guidance”, “resume help”)
- Generates context-aware responses using a **deep learning-based model**
- Flask backend for chat UI integration
- Easily extensible to new intents and responses

## 🧠 Model Pipeline
1. Text preprocessing using tokenization and stemming  
2. Training intent classification model with TensorFlow  
3. Generating responses using a mapped response dataset  
4. Flask API integration for user interaction  

## 🖼️ Output Example
**User:** "What should I learn for a data analyst role?"  
**Bot:** "You can start with Python, SQL, and Power BI, then move to statistics and data visualization tools."

## 🚀 How to Run
```bash
git clone https://github.com/<Aarzoosagar >/career-guidance-chatbot.git
cd career-guidance-chatbot
pip install -r requirements.txt
python app.py

