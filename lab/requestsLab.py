import json
import requests

res = requests.get('https://ifps-pdca-api-ifpsdemo-eks005.sa.wise-paas.com/project')
projects = res.json()
for i in range(0,len(projects)):
    print(projects[i]["ProjectName"])
    # print(projects[i].get("ProjectName"))