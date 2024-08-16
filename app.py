from flask import Flask, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define your chatbot pairs
pairs = [
    ["Hi|Hello|Hey", ["Hello!! How can I help you today?"]],
    ["I'm (.*)", ["Hello %1, how can I assist you?"]],
    ["What is your name?", ["My name is Bot, Nice to meet you"]],
    ["How are you?", ["I'm doing well, thank you for asking."]],
    ["(.*)your age?", ["I'm a computer program and do not have an age."]],
    ["Location|city ?", ["I'm Bot, I do not have any physical location."]],
    ["(.*)Let me know about(.*)?", ["Sure, %2 is located in Pedatadepalli."]],
    ["Is the Sri Vasavi Engineering College autonomous?", ["Yes, Sri Vasavi Engineering College is autonomous."]],
    ["To which university the college is affiliated?", ["Sri Vasavi Engineering College is affiliated to JNTUK."]],
    ["Is Sri Vasavi Engineering College accredited by NAAC?", ["Yes, Sri Vasavi Engineering College is accredited by NAAC with 'A' grade."]],
    ["Is Sri Vasavi Engineering College accredited by NBA?", ["Yes, Sri Vasavi Engineering College is accredited by NBA."]],
    ["Does Sri Vasavi Engineering College have a library?", ["Yes, Sri Vasavi Engineering College has a Library with good infrastructure."]],
    ["Does Sri Vasavi Engineering College have labs?", ["Yes, There are many Labs for all branches with good working systems."]],
    ["How are the classrooms?", ["Classrooms have good furnished tables and a projector for better digital visualization."]],
    ["Does Sri Vasavi Engineering College have a playground?", ["Yes, Sri Vasavi Engineering College has a playground around 400m.sq."]],
    ["Does Sri Vasavi Engineering College have a canteen?", ["Yes, Sri Vasavi Engineering College has a Mess and two private canteens."]],
    ["Are there any clubs in Sri Vasavi Engineering College?", ["Yes, there are several clubs like music, dance, photography clubs, etc."]],
    ["Are there any committees in Sri Vasavi Engineering College?", ["Yes, there are committees like anti-ragging and anti-lovers committees."]],
    ["Thank you", ["It's my pleasure"]],
    ["Bye", ["Have a nice day!"]],
]

# Create the chatbot instance
chatbot = Chat(pairs, reflections)  

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = chatbot.respond(user_message)
    
    # Ensure the response is not None
    if response is None:
        response = "I'm sorry, I didn't understand that."
    
    # Add CORS headers manually
    return (jsonify({"response": response}), 
            200, 
            {"Access-Control-Allow-Origin": "*", 
             "Access-Control-Allow-Methods": "POST", 
             "Access-Control-Allow-Headers": "Content-Type"})

@app.after_request
def add_cors_headers(response):
    # Add headers to each response
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

if __name__ == "__main__":
    app.run(debug=True)
