from flask import Flask, request, jsonify, send_from_directory
from ai import ChatBot  

app = Flask(__name__)
bot = ChatBot()


@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    if not user_message:
        return jsonify({"reply": "no message received"})
    
    response = bot.get_response(user_message)
    
    if response == "EXIT":
        return jsonify({"reply": "bye!"})
    
    return jsonify({"reply": response})

if __name__ == "__main__":  
    app.run(debug=True)