# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, Response
from WebRequestManager import WebRequestManager as webmgr
import requests
import json
import os
import dicttoxml
import datetime
import time

app = Flask(__name__)
port = 8080 #int(os.getenv("PORT"))

@app.route('/mms_DSUS/<DeviceName>/<DeviceStatus>/<Message>', methods=['GET', 'POST'])
def DSUS_MESSAGE_api(DeviceName,DeviceStatus,Message = ''):
    if request.method == 'GET': 
        print(DeviceName)
        data = '{"result":["{\"Result\":\"Success\"}"]}'
        return data
        
    elif request.method == 'POST':        
        print(request.json)
        data = '{"result":["{\"Result\":\"Success\"}"]}'
        r = Response(data,  status=200, mimetype='text/json')
        r.headers["Content-Type"] = "text/json; charset=utf-8"
        return r


@app.route('/mms_DSUS/<DeviceName>/<DeviceStatus>', methods=['GET', 'POST'])
def DSUS_api(DeviceName,DeviceStatus,Message = ''):
    if request.method == 'GET': 
        print(DeviceName)
        data = '{"result":["{\"Result\":\"Success\"}"]}'
        return data
        
    elif request.method == 'POST':        
        print(request.json)
        data = '{"result":["{\"Result\":\"Success\"}"]}'
        r = Response(data,  status=200, mimetype='text/json')
        r.headers["Content-Type"] = "text/json; charset=utf-8"
        return r


@app.route('/updateDSUS/<DeviceName>/<DeviceStatus>/<Message>', methods=['GET'])
def updateDSUS_MESSAGE_api(DeviceName,DeviceStatus,Message = ''):
    if request.method == 'GET': 
        print(DeviceName)
        data = '{"result":["{\"Result\":\"Success\"}"]}'
        return data
        

@app.route('/updateDSUS/<DeviceName>/<DeviceStatus>', methods=['GET'])
def updateDSUS_api(DeviceName,DeviceStatus,Message = ''):
    if request.method == 'GET': 
        print(DeviceName)
        data = '{"result":["{\"Result\":\"Success\"}"]}'
        return data
        



@app.route('/afus', methods=['GET', 'POST'])
def afus_post_api():
    #"""Flight Update(AFUS)"""
    if request.method == 'POST':
        data = request.json   
        xml = dicttoxml.dicttoxml(data)
        r = Response(xml,  status=200, mimetype='text/xml')
        r.headers["Content-Type"] = "text/xml; charset=utf-8"
        return r
    else:
        if request.method == 'GET':
            data = '{"API": "afus", "function": "Flight Update(AFUS)"}'
            return data


@app.route('/mms', methods=['GET'])
def mms_api():
    if request.method == 'GET':
        data = 'mms',200
        return data

@app.route('/afus/<FlightStatus>/<FlightNumber>/<SIBT>/<AIBT>/<SOBT>/<AOBT>' , methods=['GET'])
def afus_get_api(FlightStatus,FlightNumber,SIBT,AIBT,SOBT,AOBT):
    #"""Flight Update(AFUS)"""
    if request.method == 'GET':
        xml = dicttoxml.dicttoxml({'FlightStatus': FlightStatus, 'FlightNumber': FlightNumber, 'SIBT': SIBT, 'AIBT': AIBT, 'SOBT': SOBT, 'AOBT': AOBT})
        data = jsonify(xml),200
        return data


@app.route('/version',  methods=['GET'])
def version_post_api(): 
    if request.method == 'GET':
        # APPLICATION = json.loads(os.getenv("VCAP_APPLICATION"))
        # if APPLICATION['application_name'] == 'aamp-api':
        #     # responsepro = requests.get("https://aamp-api-pro.iii-cflab.com/version", False)
        #     # responsetest = requests.get("https://aamp-api-test.iii-cflab.com/version", False)
        #     # port = " pro version:" +responsepro.text + "to  test version:" +responsetest.text 
        #     # sproURL = "https://" + str(APPLICATION['application_uris'][0]).replace(str(APPLICATION['application_name']),str(APPLICATION['application_name'])+'-pro')  + "/version"
        #     # stestURL = "https://" + str(APPLICATION['application_uris'][0]).replace(str(APPLICATION['application_name']),str(APPLICATION['application_name'])+'-test')  + "/version"
        #     # port = str(sproURL)
        #     # stestURL = "https://" + APPLICATION['application_uris']+"/version".replace(APPLICATION['application_name'],APPLICATION['application_name']+'-test')
        #     responsepro = requests.get("https://" + str(APPLICATION['application_uris'][0]).replace(str(APPLICATION['application_name']),str(APPLICATION['application_name'])+'-pro')  + "/version", False)
        #     responsetest = requests.get("https://" + str(APPLICATION['application_uris'][0]).replace(str(APPLICATION['application_name']),str(APPLICATION['application_name'])+'-test')  + "/version", False)
        #     port = " pro version:" +responsepro.text + "to  test version:" +responsetest.text 
        # else:            
        port = os.getenv("version")
        return port


@app.route('/vsss',  methods=['GET', 'POST'])
def vsss_post_api():    
    #"""Video Streaming service(VSSS)"""
    if request.method == 'POST':
        data = request.json
        return jsonify(data=data, meta={"status": "ok"}),200
    else:
        if request.method == 'GET':
            # APPLICATION = json.loads(os.getenv("VCAP_APPLICATION"))
            # if APPLICATION['application_name'] ==  'aamp-api-pro':
            #     return 'Video Streaming service(VSSS)-pro'
            # else:
            #     return 'Video Streaming service(VSSS)-test'
            return 'Video Streaming service(VSSS)'
	

mmsUrl = os.getenv('MMSURL')
mmsMethod = os.getenv('MMSMETHOD').lower()
@app.route('/dsus/<DeviceID>/<DeviceStatus>',  methods=['GET', 'POST'])
def dsus_api(DeviceID, DeviceStatus):    
    #"""Device Status UPdate(DSUS)"""
    startdatetime  = datetime.datetime.now()
    start = time.time()
    sMMS = DeviceID
    if  mmsMethod == 'post':
        print(sMMS +':'+ DeviceStatus +" - "+ webmgr.post_json(mmsUrl+'/'+DeviceID+'/'+DeviceStatus, sMMS))
    elif  mmsMethod == 'get':
        print(sMMS +':'+ DeviceStatus +" - "+ webmgr.get_text(mmsUrl+'/'+DeviceID+'/'+DeviceStatus))
    end  = time.time()
    data = str(startdatetime) + ' Device Status UPdate(DSUS)- ' +sMMS +':'+ DeviceStatus +"  " +str (end-start) + 'sec'
    return data,200


@app.route('/login/<username>/<password>', methods=['GET'])
def show_user_profile(username, password):
    return jsonify({'name': username, 'words': password}),200

@app.route('/hello')
def hello_world():
    return 'Hello, World!',200


    

# @app.errorhandler(201)      
# def page_not_found(error):
#     return '---Created---', 201

# @app.errorhandler(202)      
# def page_not_found(error):
#     return '---Accepted---', 202


# @app.errorhandler(301)       
# def page_not_found(error):
#     return '---Moved Permanently---', 301
    
# @app.errorhandler(303)      
# def page_not_found(error):
#     return '---See Other---', 303


# @app.errorhandler(304)      
# def page_not_found(error):
#     return '---Not Modified---', 304

# @app.errorhandler(307)      
# def page_not_found(error):
#     return '---Temporary Redirect---', 307


@app.errorhandler(400)      
def page_not_found(error):
    return '---Bad Request---', 400

@app.errorhandler(401)      
def page_not_found(error):
    return '---Unauthorized---', 401

@app.errorhandler(403)      
def page_not_found(error):
    return '---Forbidden---', 403

@app.errorhandler(404)       
def page_not_found(error):
    return '---Not Found---', 404


@app.errorhandler(410)       
def page_not_found(error):
    return '---Gone--', 410


@app.errorhandler(500)       
def page_not_found(error):
    return '---Internal Server Error--', 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
    
    #app.run(host='127.0.0.1', port=port)