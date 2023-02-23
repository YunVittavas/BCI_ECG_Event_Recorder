import boto3
from boto3 import client
import requests

''' Variables: Initial Authorization '''

client_id :str = '4vouvmuus59a0imasgo8rcu4b1'
auth_data :dict = {'USERNAME':'testbci01', 'PASSWORD':'12345678'}
region_name :str = 'ap-southeast-1'

''' Variables: Get Url Token '''

filename = 'pytest02.txt'
filetag = 'pytest_upload02'
req_url = f'https://83mcanxyj6.execute-api.ap-southeast-1.amazonaws.com/prod-pracha/files/upload-endpoint?fileName={filename}&fileTag={filetag}'

def initAuth(ClientId, AuthParameters, region_name):
	provider_client = client('cognito-idp', region_name=region_name)
	resp = provider_client.initiate_auth(AuthFlow='USER_PASSWORD_AUTH', 
			AuthParameters=AuthParameters, ClientId=ClientId)
	return resp

def getURL(Response, RequestURL):
	access_token = Response["AuthenticationResult"]["IdToken"]
	req = requests.get(RequestURL, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(access_token) })
	return req.json()

def deleteURL(Response, RequestURL):
	access_token = Response["AuthenticationResult"]["IdToken"]
	headers = {
		'content-type': 'application/json',
		'Authorization': 'Bearer {}'.format(access_token),
		'Cache-Control': 'no-cache'
	}
	#req = requests.delete(RequestURL, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(access_token)})
	req = requests.delete(RequestURL, headers=headers)
	return req.json()	
	
def uploadFile(UploadURL, Files, Fields):
	post = requests.post(url, files=Files, data=Fields)
	return post
	
resp = initAuth(client_id, auth_data, region_name)
delete = deleteURL(resp, req_url)
print(delete)

#req = getURL(resp, req_url)

#url = req['bucketDetail']['url']
#fields = req['bucketDetail']['fields']
#files = {'file': open(f'/home/pi/Desktop/{filename}','rb')}

#post = uploadFile(url, files, fields)
#print(post)



