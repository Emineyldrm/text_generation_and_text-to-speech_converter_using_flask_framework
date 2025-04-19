from gtts import gTTS
import os
import uuid #Python'daki uuid kütüphanesini kullanarak benzersiz bir dosya adı oluşturduk

def create_audio(response,language):
    myText = response
    #language = "tr"

    myobj = gTTS(text=myText, lang=language, slow=False)

   # myobj.save('ses.mp3')
    # Benzersiz bir dosya adı oluştur
    unique_filename = str(uuid.uuid4()) + ".mp3"
    file_path = os.path.join("static", unique_filename)
    myobj.save(file_path)
    return unique_filename


# Ses dosyası kodun derlendiğinde çalışmaması için kapatıldı. 
# os.system("start ses.mp3")




# def ses_dosyasi(response):
#     myText = response
#     language = "tr"
#     myobj = gTTS(text=myText, lang=language, slow=False)
#    # myobj.save('ses.mp3')
#     # Benzersiz bir dosya adı oluştur
#     unique_filename = str(uuid.uuid4()) + ".mp3"
#     file_path = os.path.join("static", unique_filename)
#     myobj.save(file_path)
#     return unique_filename
    