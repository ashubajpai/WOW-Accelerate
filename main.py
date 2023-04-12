import os
import openai
import gradio

from flask import Flask
app = Flask(__name__)

messages = []
messages.append({"role": "system", "content": "You are a Scrum Master who specializes in WOW practices"})

@app.route("/")
def hello_world():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    demo = gradio.Interface(fn=chatbot, inputs = ["text",'state'], outputs = ["chatbot", 'state'], title = "WOW-Accelerate")
    demo.launch(share=False)

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

def chatbot(input, history=[]):
    output = CustomChatGPT(input)
    history.append((input,output))
    return history, history

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))