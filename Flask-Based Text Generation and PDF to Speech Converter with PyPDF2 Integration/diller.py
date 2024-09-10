from gtts.lang import tts_langs

diller = tts_langs()
for dil_kodu, dil_adi in diller.items():
    print(f"{dil_kodu}: {dil_adi}")


# <!-- {% for dil_kodu, dil_adi in diller.items() %}
#                       <option value="{{ dil_kodu }}">{{ dil_adi }}</option>
#                       {% endfor %} -->
#                       <!-- {% for lang_code, lang_name in diller.items() %}
#                       <option value="{{ lang_code }}">{{ lang_name }}</option>
#                       {% endfor %} -->