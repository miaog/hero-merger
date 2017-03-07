from flask import Flask, request, abort, jsonify, Response, json
from data import *
from hero_merger import *
import uuid
app = Flask(__name__)

channel_key = '6Wr1sR6btsGaqIwCejGxjv-Zyh2QP7BBU-WZ4m4MSIqos4CF1yKeolBTa6QyygVj'
url_prefix = "https://919cc80d.ngrok.io/"

@app.route('/ifttt/v1/status')
def status():
    if request.headers["IFTTT-Channel-Key"] != channel_key:
        err = Response(json.dumps(error_channel_key), mimetype='application/json; charset=utf-8')
        err.status_code = 401
        return err
    else:
        return "Good"

@app.route('/ifttt/v1/test/setup', methods=['POST'])
def setup():
    if request.headers["IFTTT-Channel-Key"] != channel_key:
        err = Response(json.dumps(error_channel_key), mimetype='application/json; charset=utf-8')
        err.status_code = 401
        return err
    if request.method == "POST":  
        return Response(json.dumps(sample), mimetype='application/json; charset=utf-8')
    else:
        abort(404)

@app.route('/ifttt/v1/triggers/any_new_hero', methods=['POST'])
def trigger_any_new_hero():

    if request.headers["IFTTT-Channel-Key"] != channel_key:
        err = Response(json.dumps(error_channel_key), mimetype='application/json; charset=utf-8')
        err.status_code = 401
        return err
    if request.method == "POST":  
        data = request.data
        dataDict = json.loads(data)
        if "limit"in dataDict:
            return Response(json.dumps({"data": heroes_data["data"][::-1][:dataDict["limit"]]}), mimetype='application/json; charset=utf-8')
        return Response(json.dumps({"data": heroes_data["data"][::-1]}), mimetype='application/json; charset=utf-8')
    else:
        abort(404)

@app.route('/ifttt/v1/actions/generate_a_hero', methods=['POST'])
def actions_create_new_things():

    if request.headers["IFTTT-Channel-Key"] != channel_key:
        err = Response(json.dumps(error_channel_key), mimetype='application/json; charset=utf-8')
        err.status_code = 401
        return err
    if request.method == "POST":  
        data = request.data
        dataDict = json.loads(data)
        if "gender"in dataDict["actionFields"]:
            gender = dataDict["actionFields"]["gender"]
            new_hero = generate_hero(gender)
        else:
            new_hero = generate_hero()
        hero_id = uuid.uuid1().hex
        generated_heroes[hero_id] = new_hero
        return Response(json.dumps(
            {"data": [{"id": hero_id, "url": url_prefix + "ifttt/v1/get_hero/"+ hero_id}]}),
            mimetype='application/json; charset=utf-8')
    else:
        abort(404)

@app.route('/ifttt/v1/get_hero/<hero_id>')
def get_hero(hero_id):
    if hero_id in generated_heroes:
        return Response(json.dumps(generated_heroes[hero_id]),mimetype='application/json; charset=utf-8')
    else:
        return "Error: hero not found"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)