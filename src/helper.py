import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY


def voice_input():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('You asked : ', text)
        return text
    except sr.UnknownValueError:
        print("Sorry, couldn't understand the audio")
    except sr.RequestError as e:
        print("couldn't request result from google speech recognition service: {0}".format(e))


def llm_model_object(user_input_text):

    # print(os.environ['GOOGLE_API_KEY'])
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

    model = genai.GenerativeModel("models/gemini-pro")

    response = model.generate_content(user_input_text)

    result = response.text

    return result


def text_to_speech(text):
    
    txt_to_speech = gTTS(text=text,lang='en')

    txt_to_speech.save('output_speech.mp3')

