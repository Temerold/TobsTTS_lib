import os
import sys
clear = lambda: os.system('cls')

x = 0
while x == 0:
    try:
        os.system('pip install gtts')
        os.system('pip install playsound')
        x = 1
    except:
        try:
            os.sytem("py -m pip install gtts")
            os.sytem("py -m pip install playsound")
            x = 1
        except OSError as e:
            y = 0
            while y == 0:
                print(e)
                ign = input("Kunde inte installera 3rd party moduler. Vill du försöka igen? (y/n):\n")
                if ign == "n":
                    sys.exit()
                elif ign != "y" or ign != "n":
                    print("\nSvara endast med \"y\" eller \"n\".")
                else:
                    y = 1
clear()
try:
    from gtts import gTTS
    from playsound import playsound
except ImportError:
    print(ImportError)
    input("Kunde inte importera 3rd party moduler.")
    sys.exit()


def tts(msg, language, filnamn="Tob's TTS no_name"):
    try:
        obj = gTTS(text = msg, lang = language, slow = False)
        obj.save(filnamn + ".mp3")
    except:
        y = 0
        while y == 0:
            ign = input("Kunde inte spara fil \"" + filnamn + ".mp3" + "\". Vill du försöka igen? (y/n):\n")
            if ign == "n":
                sys.exit()
            elif ign != "y" or ign != "n":
                print("\nSvara endast med \"y\" eller \"n\".")
            else:
                y = 1
        
def say(fil):
    try:
        playsound(fil)
    except:
        print("Fil inte hittad.")
    
