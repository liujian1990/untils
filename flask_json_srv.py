from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def service():
    if request.method == 'POST':
        data = request.get_json()
        print json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
        return "Json OK."
    return "Web OK."

if __name__ == 'main':
    app.run('0.0.0.0', '8001')