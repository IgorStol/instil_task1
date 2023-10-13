import math
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def summa():
    i= request.get_json()
    value1 = i['value1']
    value2 = i['value2']
    res = value1 + value2
    return jsonify({'result': res})

@app.route('/dif', methods=['POST'])
def minus():
    i= request.get_json()
    value1 = i['value1']
    value2 = i['value2']
    res = value1 - value2
    return jsonify({'result': res})

@app.route('/exp', methods=['POST'])
def exponentiation():
    i = request.get_json()
    value1 = i['value1']
    value2 = i['value2']
    res = pow(i['value1'], i['value2'])
    return jsonify({'result': res})

@app.route('/abs', methods=['POST'])
def abs():
    i = request.get_json()
    value = i['value']
    if value >= 0:
        res = math.sqrt(value)
        return jsonify({'result': res})
    else:
        return print('Некорректное значение')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)