import math
import random

class ChatBot:
    def __init__(self):
        self.name = ""
        self.history = []

    def ai_response(self, inp):
        try:
            import ollama   
            messages = [
                {"role": "system", "content": "You are an AI assistent bot named zoe, ur task is to act like the users assistant and give answers in medium length and to the point, always answer in lowercase, and dont give extra information, talk like you are close with the user, give answer in points and indentations"}
            ]
            messages.extend(self.history[-6:])
            messages.append({"role": "user", "content": inp})
            response = ollama.chat(
                model="phi3",
                messages=messages 
            )
            return "Bot: " + response["message"]["content"]

        except Exception as e:
            return f"Bot error: {e}"

    def extract_name(self, inp):
        inp_lower = inp.lower()
        if "my name is" in inp_lower: 
            return inp_lower.split("my name is")[-1].strip()
        elif "i am" in inp_lower:
            return inp_lower.split("i am")[-1].strip()
        elif "i'm" in inp_lower:
            return inp_lower.split("i'm")[-1].strip()
        return ""

    def handle_greeting(self, inp):
        response = ""
        if any(word in inp.lower() for word in ["hello", "yo", "hi"]):
            r = random.randint(1,3)
            if self.name == "":
                if r==1:
                    response = "Bot: hello user!"
                elif r==2:
                    response = "Bot: yo user!"
                else:
                    response = "Bot: hi user!"
            else:
                if r==1:
                    response = f"Bot: hello {self.name.title()}"
                elif r==2:
                    response = f"Bot: yo {self.name.title()}"
                else:
                    response = f"Bot: hi {self.name.title()}"
        return response

    def handle_history(self):
        if self.history:
            return f"Bot: last snippet:\n {self.history[-1]}"
        else:
            return "Bot: you haven't said anything yet"

    def handle_name_query(self):
        if self.name != "":
            return f"Bot: your name is {self.name}" 
        else: 
            return "Bot: you've not told me your name yet!"

    def handle_help(self):
        return "Bot: i'm a work in progress AI bot :)"

    def commands(self, inp):
        if inp.lower() == "help": 
            return " /help -> list all commands \n /history -> shows query history\n /clear -> delete history"
        elif inp.lower() == "history":
            return "history: " + str(self.history)
        elif inp.lower() == "clear":
            self.history = []
            return "history deleted"
        return False

    def detect_intent(self, inp):
        inp_lower = inp.lower()
        intents = {
            "greeting": ["hello","hi","hey","sup","whatsup"],
            "help": ["help","assist","what can you do"],
            "name_query": ["name","my"],
            "history": ["before","previous"],
            "exit": ["bye","goodbye","quit","exit"]
        }
        for intent, words in intents.items():
            for word in words:
                if word in inp_lower:
                    return intent
        return "unknown"

    def get_response(self, inp):
        # check commands first
        if inp.startswith("/"):
            temp = self.commands(inp[1:])
            return temp if temp else ""

        new_name = self.extract_name(inp)
        if new_name:
            self.name = new_name
            return f"Bot: nice to meet you"

        intent = self.detect_intent(inp)

        if intent == "greeting":
            response = self.handle_greeting(inp)
        elif intent == "name_query":
            response = self.handle_name_query()
        elif intent == "history":
            response = self.handle_history()
        elif intent == "help":
            response = self.handle_help()
        elif intent == "exit":
            response = "EXIT"
        else:
            response = self.ai_response(inp)

        self.history.append({"role": "user", "content": inp})
        self.history.append({"role": "assistant", "content": response.replace("Bot: ","")})

        return response

if __name__ == "__main__":
    bot = ChatBot()
    while True:
        inp = input("User: ")
        response = bot.get_response(inp)
        if response == "EXIT":
            print("Bot: bye User!")
            break
    print(response)