import pyttsx3
import PyPDF2
from gtts import gTTS


pdfReader=PyPDF2.PdfFileReader(open('jk.pdf','rb'))
engine = pyttsx3.init()

engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume',2)


for page in range(pdfReader.numPages):
    t=pdfReader.getPage(page).extractText()
    engine.say(t)
    engine.runAndWait()

tts=gTTS(text=t, lang='en')
tts.save("jk.mp3")
print("sucesss")
engine.runAndWait()
engine.stop()
