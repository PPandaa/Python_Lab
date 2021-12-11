import os
import requests
from dotenv import load_dotenv

res = requests.get('https://ifps-pdca-api-ifpsdemo-eks005.sa.wise-paas.com/project')
projects = res.json()
for i in range(0,len(projects)):
    print(projects[i]["ProjectName"])
    # print(projects[i].get("ProjectName"))

# load env
load_dotenv(dotenv_path="local.env")

logString = 'Dependencies Info.\n'

IFP_DESK_API_URL = os.getenv('IFP_DESK_API_URL')
if IFP_DESK_API_URL:
    logString += '  IFP_DESK_API_URL: ' + IFP_DESK_API_URL + '\n'

IFP_DESK_CLIENT_SECRET = os.getenv('IFP_DESK_CLIENT_SECRET')
if IFP_DESK_CLIENT_SECRET:
    logString += '  IFP_DESK_CLIENT_SECRET: ' + IFP_DESK_CLIENT_SECRET + '\n'

print(logString)

# set request body
variables = {
    'groupId': 'R3JvdXA.YJ3ZKZYEDgAHH1MW',
    'relationKeys': ['EHS.Electricity'],
    'years': [2021],
    'kinds': ['DayWeekday','DayHoliday']
}

requestBody = {
    'variables': variables,
    'query': '''query ($groupId: ID!, $relationKeys: [String!]!, $years: [NonNegativeInt!]!, $kinds: [GenericKpiKind!]!) { 
		group(id: $groupId) {
			id
		    genericKpiList(relationKeys: $relationKeys, years: $years, kinds: $kinds) {
		        id
		        relationKey
		        kind
		        year
		        hour
		        kpi
		    }
		}
	}'''
}

# set request header
headers = {'X-Ifp-App-Secret': IFP_DESK_CLIENT_SECRET}

# process response
res = requests.post(IFP_DESK_API_URL,json=requestBody,headers=headers)
if res.status_code != 200 :
    print(res)
else:
    resJSON = res.json()
    if 'errors' in resJSON :
        print(resJSON['errors'])
    else :
        print(resJSON['data'])