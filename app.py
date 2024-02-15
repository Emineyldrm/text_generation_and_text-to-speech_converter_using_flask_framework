from flask import Flask,render_template, request
from text_generation import generate_text_from_question
from text_to_speech import create_audio


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/submit', methods=['POST'])
def submit():
    soru = request.form['soru']
    response = generate_text_from_question(soru)
    create_audio(response)
    return render_template('sonuc.html', soru=soru, response=response)

if __name__=='__main__':
    app.run(debug=True)




    