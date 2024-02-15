# text_generation.py

from click import prompt
import openai
from config import openai_api_key 
openai.api_key = openai_api_key


def generate_text_from_question(question):
    model_engine = "gpt-3.5-turbo-instruct"
    #model_engine = "gpt-3.5-turbo"
    #model_engine ="davinci-002"     

    #model_engine="davinci-text-003"    #:(
    #chatgpt ai yi tanımladık

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=question,
        max_tokens=1024,
        n=1, #kaç farklı cevap
        #stop=None,
    )
    response = completion.choices[0].text

    return response
