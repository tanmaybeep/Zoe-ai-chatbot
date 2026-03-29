# Zoe - Terminal AI Chatbot

A terminal-style AI chatbot built from scratch with a custom backend, API layer, and frontend.

This project focuses on building a **system around AI**, not just calling a model.

---

## Features

- Custom chatbot logic (intents, commands, memory)
- AI integration using Ollama (Llama 3)
- Flask API connecting backend and frontend
- Terminal-style UI with:
  - Boot sequence
  - Spinner animation
  - Real-time typing effect
- Command system:
  - `/help`
  - `/history`
  - `/clear`

---

## Tech Stack

- Python
- Flask
- JavaScript
- HTML/CSS
- Ollama (Llama 3)

---

## Project Structure
zoe-chatbot/
│
├── app.py # Flask API
├── chatbot.py # ChatBot class (logic + AI)
├── requirements.txt
├── README.md
│
├── templates/
│ └── index.html # Frontend UI
│
└── static/ # (optional for future css/js split)

## How It Works

1. User sends input from the browser  
2. Flask API receives the request (`/chat`)  
3. ChatBot processes the input:
   - checks commands (`/help`, `/clear`)
   - detects intent (greeting, name, etc.)
   - falls back to AI if needed  
4. Ollama generates a response  
5. Response is returned to frontend  
6. UI displays it with typing animation  

---

## Setup

### 1. Clone the repository

git clone https://github.com/your-username/zoe-chatbot.git
cd zoe-chatbot

### 2. Install dependencies

pip install -r requirements.txt

### 3. Intsall and run Ollama

ollama run llama3

### 4. Start the Flask server

python app.py

### 5. open in browser

http://127.0.0.1:5000

## Future Improvements:

deploy online (public access)
better memory handling (context trimming / summaries)
improved intent detection
authentication / user sessions
integrate maze solver into chatbot

## Key take away:
AI is just the brain.
The real value comes from how you design the system around it.

## Author: 
Tanmay Jagtap
