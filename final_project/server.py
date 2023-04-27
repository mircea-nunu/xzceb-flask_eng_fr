'''Server'''
import json
from flask import Flask, render_template, request
from machinetranslation import translator



app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    '''EndPoint englishToFrench'''
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.english_to_french(text_to_translate)
    return translated_text # "Translated text to French"

@app.route("/frenchToEnglish")
def french_to_english():
    '''EndPoint frenchToEnglish'''
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.french_to_english(text_to_translate)
    return translated_text #"Translated text to English"

@app.route("/")
def render_index_page():
    '''Route Home'''
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
