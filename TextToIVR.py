import gtts
import os
import subprocess

def speak(audioString):
    #Text To Speech from audioString
    tts = gtts.gTTS(text=audioString, lang="th", slow=False)
    
    #Check and Make Dir RAW
    if not os.path.exists("RAW"):
        try:
            os.makedirs("RAW")
        except OSError:
            print("Create Dir[RAW] Failed")
        else:
            print("Create Dir[RAW] Success")

    #Save MP3 
    path = os.getcwd()
    rawmp3 = path + "\\RAW\\" + audioString + ".mp3"
    tts.save(rawmp3)    
    print(rawmp3 + "\n")

    #Play Audio
    os.system(r"sox\mpg123.exe -q " + path + "\\RAW\\" + audioString + ".mp3")

    #Convert MP3 to WAV
    savefilename = input("Save to WAV file: ")
    wave_output = path + "\\WAV\\" + savefilename + ".wav"

    #Check and Make Dir WAV
    if not os.path.exists("WAV"):
        try:
            os.makedirs("WAV")
        except OSError:
            print("Create Dir[WAV] Failed")
        else:
            print("Create Dir[WAV] Success")

    #Save WAV
    try:
        subprocess.call([r"sox\sox", rawmp3, "-e", "mu-law", "-r", "8k", wave_output, "remix", "1"])
    except:
        print("[ERROR !!]")
    else:
        print("[SAVED !] " + path + "\\WAV\\" + savefilename + ".wav\n")

print("\nText-TO-IVR By Kritsana Kleebkaew\n")
while True:    
    text = str(input("Text To Speech: "))
    speak(text)