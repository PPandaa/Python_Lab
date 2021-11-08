from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

#Type 1
@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        print(request)
        return jsonify(request.json)
    elif request.method == "GET":
        print(request)
        name = request.args.get('name')
        return "Hello"+name

if __name__ == '__main__':
    app.debug = True
    app.run()