import requests
import json
import smartsheet as ss

# Getting QAR ID's that need to be entered

response = requests.get(
    'http://10.192.40.56:10006/restapi/fitapp/getBugList?groupSize=1000?filterStruct?mStatus=Open'
)
response.raise_for_status()
jsonResponse = response.json()
bugCount = int(jsonResponse["totalCount"])

qarList = []

for i in range(bugCount):
    qarList.append(int(jsonResponse["bugStructList"][i]["bugStruct"]["mId"]))
#   print(jsonResponse["bugStructList"][i]["bugStruct"]["mId"])

qarList.sort()
#print(qarList)

var = input("Pleaser enter something: ")
print("You entered: " + var)
