from flask import Flask, request, jsonify, Response
import os
import dicttoxml



app = Flask(__name__)
port = int(os.getenv("PORT"))
"""Flight Update(AFUS)"""
@app.route('/afus', methods=['POST'])
def afus_post_api():
    data = request.json
    xml = dicttoxml.dicttoxml(data)
    r = Response(xml,  status=200, mimetype='text/xml')
    r.headers["Content-Type"] = "text/xml; charset=utf-8"
    return r

	
"""Video Streaming service(VSSS)"""
@app.route('/vsss', methods=['POST'])
def vsss_post_api():
    data = request.json
    return jsonify(data=data, meta={"status": "ok"}),200
	
"""Tow Car Status Distribution(TCSD)"""
@app.route('/tcsd', methods=['POST'])
def tcsd_post_api():
    data = request.json
    return jsonify(data=data, meta={"status": "ok"}),200

"""Device Status UPdate(DSUS)"""
@app.route('/dsus', methods=['POST'])
def dsus_post_api():
    data = request.json
    return jsonify(data=data, meta={"status": "ok"}),200


"""CCTV 航機偵測服務(CCTV)"""
@app.route('/cctv', methods=['POST'])
def cctv_post_api():
    data = request.json
    return jsonify(data=data, meta={"status": "ok"}),200


@app.route('/login/<username>/<password>', methods=['GET'])
def show_user_profile(username, password):
    return jsonify({'name': username, 'words': password}),200
@app.route('/hello')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=port)