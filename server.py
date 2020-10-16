from sanic import Sanic
from sanic.response import json
from sanic.response import text
from process_img import *
app = Sanic("")

@app.route("/api/devices/")
async def alldetails(request):
    try:
        wifi_resp = wifi(None)
        ble_resp = ble(None)
        jsonresp = {"wifi":wifi_resp,"ble":ble_resp}
        return json(jsonresp)
    except Exception as e:
        return json({"message":"server error","error":str(e)})

@app.route("/api/devices/<device>")
async def details(request,device):
    try:
        if device=='wifi':
            wifi_resp = wifi(None)
            jsonresp = {"wifi":wifi_resp}
            return json(jsonresp)
        elif device=='ble':
            ble_resp = ble(None)
            jsonresp = {"ble":ble_resp}
            return json(jsonresp)
        else:
            return json({"message":"device not found"})
        wifi_resp = wifi(None)
        ble_resp = ble(None)
        jsonresp = {"wifi":wifi_resp,"ble":ble_resp}
        return json(jsonresp)
    except Exception as e:
        return json({"message":"server error","error":str(e)})

@app.route("/api/devices/<device>/<dev_id>")
async def wifiid(request,device,dev_id):
    try:
        if device=='wifi':
            wifi_resp = wifi(dev_id)
            jsonresp = {"wifi":wifi_resp}
            return json(jsonresp)
        elif device=='ble':
            ble_resp = ble(dev_id)
            jsonresp = {"ble":ble_resp}
            return json(jsonresp)
        else:
            return json({"message":"device not found"})
        return json(jsonresp)
    except Exception as e:
        return json({"message":"server error","error":str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0",access_log=False, port=8000)