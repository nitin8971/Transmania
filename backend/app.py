from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    from_lang = data['from_lang']
    to_lang = data['to_lang']
    text = data['text']

    translator = Translator()
    translated_text = translator.translate(text, src=from_lang, dest=to_lang)

    return jsonify({"translated_text": translated_text.text})

if __name__ == '__main__':
    app.run(debug=True)
