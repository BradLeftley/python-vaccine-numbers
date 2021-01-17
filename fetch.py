import requests
import json
import boto3

response = requests.get('https://coronavirus.data.gov.uk/api/v1/data?filters=areaName=United%2520Kingdom;areaType=overview&latestBy=cumPeopleVaccinatedFirstDoseByPublishDate&structure=%7B%22date%22:%22date%22,%22value%22:%22cumPeopleVaccinatedFirstDoseByPublishDate%22%7D')
print (response.status_code)
data = response.json()
d = json.dumps(data)
print(data['data'])

s3 = boto3.resource(
    's3',
    region_name='eu-west-2',
    aws_access_key_id='',
    aws_secret_access_key=''
)
content = data['data']
s3.Object('', 'data.json').put(Body=str(json.dumps(content)))
