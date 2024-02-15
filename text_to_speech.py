from gtts import gTTS
import os

def create_audio(response):
    myText = response
    language = "tr"

    myobj = gTTS(text=myText, lang=language, slow=False)

   # myobj.save('ses.mp3')
    file_path = os.path.join("static", "ses.mp3")
    myobj.save(file_path)

# Ses dosyası kodun derlendiğinde çalışmaması için kapatıldı. 
# os.system("start ses.mp3")
