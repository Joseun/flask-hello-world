from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"slackUsername": "Joseun",
                    "backend": True,
                    "age": 27,
                    "bio": "Hi, Joseph Ologunja here, I am a Full Stack developer, proficient in Python"
                   })

@app.route('/', methods=['POST'])
def hello_world():
     if not request.get_json():
        abort(400, description="Not a JSON")

    if 'operation_type' not in request.get_json():
        abort(400, description="Missing operation_type")
    if 'x' not in request.get_json():
        abort(400, description="Missing value")
    if 'y' not in request.get_json():
        abort(400, description="Missing value")
    if type(x) not int:
        abort(400, description="Value not an integer")
    if type(y) not int:
        abort(400, description="Value not an integer")
    ops = {'addition': x + y, 
           'substraction': x - y,
           'multiplication': x * y}
    data = request.get_json()
    for k, v in ops:
        if k = data['operation_type']:
            result = v
   
    return jsonify({"slackUsername": "Joseun",
                    "operation_type": data['operation_type'],
                    "result": result
                   })
