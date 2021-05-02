#!/usr/local/bin/python3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
from flask import Flask, abort, jsonify, request
#from flask_cors import CORS, cross_origin
import tensorflow as tf
import gpt_2_simple as gpt2

if not os.path.exists('models'):
    gpt2.download_gpt2(model_name="355M")

app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

#keras.backend.clear_session()d
print("GPT downloaded")
sess = gpt2.start_tf_sess()
print("session started")
gpt2.load_gpt2(sess, run_name='run1')
print("checkpoint loaded")

graph = tf.get_default_graph()

def getResponse(msg, prefixHistory):
    global graph
    prefixHistory += "Person: " + msg + "\n" + "Aryeh Bookbinder:"
    print(prefixHistory)
    with graph.as_default():
        text = gpt2.generate(sess, length=25,temperature=0.7,prefix=prefixHistory, return_as_list=True)[0]
    print(prefixHistory,  text)
    text = text[len(prefixHistory):]
    print(prefixHistory,  text)
    botResponse = "Aryeh Bookbinder:" + text
    #prefixHistory += botResponse
    end = text.find("Person") 
    return (text[:end-1]), prefixHistory

@app.route("/generate", methods=['POST'])
#@cross_origin()
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
        response, _ = getResponse(data['text'], data['prefixHistory'])
        #result = response.replace("Aryeh Bookbinder", "Aryeh Bot")
        return jsonify({'result': "Aryeh Bookbinder:" + str(response)})

@app.route('/test', methods=['POST'])
def test_response():
    return 'Done', 201 