#!/usr/local/bin/python3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin
from tensorflow import keras
import gpt_2_simple as gpt2
from .run_generation import generate_text

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
gpt2.download_gpt2(model_name="355M")

def getResponse(msg):
    prefixHistory = ""
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
    prefixHistory += "Person: " + msg + "\n" + "Aryeh Bookbinder:"
    #print(sess, msg, prefixHistory)P+
    text = gpt2.generate(sess, length=200,temperature=0.6,prefix=prefixHistory, return_as_list=True)[0]
    text = text[len(prefixHistory):]
    botResponse = "Aryeh Bookbinder:" + text
    prefixHistory += botResponse
    end = text.find("Person") 
    return (botResponse[:end-1]), prefixHistory

@app.route("/generate", methods=['POST'])
@cross_origin()
def get_gen():
    data = request.get_json()

    if 'text' not in data or len(data['text']) == 0 or 'model' not in data:
        abort(400)
    else:
        # text = data['text']
        # model = data['model']

        # result = generate_text(
        #     model_type='gpt2',
        #     length=100,
        #     prompt=text,
        #     model_name_or_path=model
        # )
        response, _ = getResponse(data['text'])
        print(response)
        result = response.replace("Aryeh Bookbinder", "Aryeh Bot")
        return jsonify({'result': result})

@app.route('/test', methods=['POST'])
def test_response():
    return 'Done', 201 