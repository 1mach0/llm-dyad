import os

f = open('context.txt', 'r')

def respond(incoming):
    import pip._vendor.requests as requests

    MODEL = "qwen3.5:4b"
    OLLAMA = "http://localhost:11434/api/generate"

    with open('context.txt', 'r') as file:
        context = file.read() 

    r = requests.post(OLLAMA, json={
        "model": MODEL,
        "prompt": f"Someone texted me: {incoming} and you have this context: {context}",
        "system": "You are the person responding to this message"
        "output ONLY the reply text and nothing else."
        "if you feel unsure about your answers, just say youre not sure"
        "dont have any emojis, you can use ascii emoticons but only rarely",
        "stream": False 
    })

    print(r.json()['response'].strip())

respond("hello, good morning!")

def get_messages(path):
