import gtts
import os

def speak(audioString):
    tts = gtts.gTTS(text=audioString, lang="th", slow=False)
    tts.save("audio.mp3")
    os.system("mpg123.exe -q audio.mp3")

text = str(input("Insert Thai Text: "))
while text not in ("exit", "Exit", "ออก"):
    speak(text)
    text = str(input("Insert Thai Text: "))