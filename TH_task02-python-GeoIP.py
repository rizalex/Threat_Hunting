import urllib.request
import json

ipAddr = open("All_IP.txt","r")
for ip in ipAddr:
    response = urllib.request.urlopen("http://extreme-ip-lookup.com/json/" + ip)
    geo = json.load(response)
    print(ip + geo["country"])
