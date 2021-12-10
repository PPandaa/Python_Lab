import json
import requests

res = requests.get('https://ifps-pdca-api-ifpsdemo-eks005.sa.wise-paas.com/project')
projects = res.json()
for i in range(0,len(projects)):
    print(projects[i]["ProjectName"])
    # print(projects[i].get("ProjectName"))

# variables = '{"groupId": "R3JvdXA.YJ3ZKZYEDgAHH1MW"}'
# requestBody = {
#     'variables': variables, 
#     'query': 'query ($groupId: ID!) { group(id: $groupId) { id name } }'
# }
# headers = {'X-Ifp-App-Secret': 'OWFhYThkZWEtOGFjZS0xMWViLTk4MzItMTZmODFiNTM3OTI4'}
# res = requests.post("https://ifp-organizer-dmd-eks009.sa.wise-paas.com/graphql",data=requestBody,headers=headers)
# print(res)
# resJSON = res.json()
# if 'errors' in resJSON :
#     print(resJSON['errors'])
# else :
#     print(resJSON['data'])