import json
import yaml
with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)
print("El tokende acceso es : {}".format(ourjson['access_token']))
print("El token expira en {} seconds.".format(ourjson['expires_in']))
