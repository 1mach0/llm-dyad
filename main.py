# Source - https://stackoverflow.com/a/69374234
# Posted by Murat Büyükaksu
# Retrieved 2026-04-18, License - CC BY-SA 4.0

import pip._vendor.requests as requests

def respond(question):
    return "answer answer answer"

MODEL = "qwen3.5:4b"
OLLAMA = "http://localhost:11434/api/generate"

r = requests.post(OLLAMA, json={
    "model": MODEL,
    "prompt": "Someone texted me: 'question question question';\
            you are the one responding to the texts,\
            reply on my behalf",
    "stream": False 
})

print(r.json()['response'].strip())