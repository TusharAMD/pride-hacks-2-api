import pickle
import spacy
import flask

try:
        nlp = spacy.load("en_core_web_md")
except:
    spacy.cli.download("en_core_web_md")
    nlp = spacy.load("en_core_web_md")
    

from flask import Flask,request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


@app.route('/api',methods = ['POST', 'GET'])
@cross_origin()
def api():
    
    if request.method == 'POST':
      text = request.json["text"]
      print(text)
      

    nlp = spacy.load("en_core_web_md")
    loaded_model = pickle.load(open("model.sav", 'rb'))
    #test_x = ["fags should not be allowed", "gays are unnatural", "happy pride month", "having lgbt friend is awesome"]
    test_x = [text]
    print(test_x)
    test_docs = [nlp(text) for text in test_x]
    test_x_word_vectors =  [x.vector for x in test_docs]
    value = loaded_model.predict(test_x_word_vectors)[0]
    print(value)
    return {"value":value}

if __name__ == '__main__':
    app.run(debug=True)

    
