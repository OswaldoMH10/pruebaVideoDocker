# class Calculator:
#     def sum(self, a: int, b: int) -> int:
#         return a + b
from flask import Flask, request, jsonify

class Calculator:
    def sum(self, a: int, b: int) -> int:
        return a + b

app = Flask(__name__)
calculator = Calculator()

@app.route('/')
def home():
    return "¡Calculadora funcionando! Usa /sum?a=5&b=3"

@app.route('/sum')
def sum_route():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        result = calculator.sum(a, b)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Parámetros inválidos"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)