import os
import json
import requests
from gtts import gTTS

API_KEY = "    "
# නවතම Gemini 3.8 Flash API Endpoint එක වෙත යාවත්කාලීන කරන ලදී
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={API_KEY}"

def speak(text):
    print(f"\nNEXUS: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("termux-media-player play response.mp3")

def listen():
    print("\n----------------------------------------")
    user_text = input("You (Type your command to NEXUS): ")
    return user_text

def ask_nexus(prompt):
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{
            "parts": [{"text": f"You are NEXUS, an advanced futuristic AI assistant like Iron Man's Jarvis. Answer shortly and smartly: {prompt}"}]
        }]
    }
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        res_json = response.json()
        
        if "candidates" in res_json:
            reply = res_json['candidates'][0]['content']['parts'][0]['text']
            return reply
        elif "error" in res_json:
            print(f"API Error Details: {res_json['error'].get('message', 'Unknown error')}")
            return "My core systems encountered an API error."
        else:
            return "I received an unexpected response from my servers."
            
    except Exception as e:
        print(f"Connection Error: {e}")
        return "I am having trouble connecting to my core systems."

if __name__ == "__main__":
    speak("NEXUS systems online. How can I assist you today?")
    
    while True:
        user_input = listen()
        if user_input:
            if "exit" in user_input.lower() or "quit" in user_input.lower():
                speak("Shutting down systems. Goodbye!")
                break
            
            ai_reply = ask_nexus(user_input)
            speak(ai_reply)
