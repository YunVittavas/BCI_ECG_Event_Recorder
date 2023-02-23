import boto3
from boto3 import client
import requests

class ER_CloudUpload():
	def __init__(self):
		''' Variables: Initial Authorization '''
		self.__clientID :str = ''
		self.__authData :dict = {}
		self.__regionName :str = ''
		self.__response :dict = {}
		
		''' Variables: Get Url Token '''
		self.__fileName :str = ''
		self.__fileTag :str = ''
		self.__reqURL :str = ''
		self.__request :dict = {}
		
		''' Variables: Upload File '''
		self.__uploadURL :str = self.__request['bucketDetail']['url']
		self.__uploadFields :dict = self.__request['bucketDetail']['fields']
		self.__uploadFiles :dict = {'file': open(f'/home/pi/Desktop/{filename}','rb')}
		
	''' Getter and Setter of Initial Authorization '''
	@property
	def clientID(self):
		return self.__clientID
		
	@clientID.setter
	def clientID(self, ID):
		if isinstance(ID, str) and not isinstance(ID, bool):
			self.__clientID = ID
		else:
			self.__clientID = -1
		return self.__clientID
		
	@property
	def authData(self):
		return self.__authData
		
	@authData.setter
	def authData(self, AUTH):
		if isinstance(AUTH, dict) and not isinstance(AUTH, bool):
			self.__authData = AUTH
		else:
			self.__authData = -1
		return self.__authData
		
	@property
	def regionName(self):
		return self.__regionName
	
	@regionName.setter
	def regionName(self, NAME):
		if isinstance(NAME, str) and not isinstance(NAME, bool):
			self.__regionName = NAME
		else:
			self.__regionName = -1
		return self.__regionName

	@property
	def response(self):
		return self.__response
	
	@response.setter
	def response(self, RESPONSE):
		if isinstance(RESPONSE, dict) and not isinstance(RESPONSE, bool):
			self.__response = RESPONSE
		else:
			self.__response = -1
		return self.__response

''' Getter and Setter of Getting URL Token '''
	@property
	def fileName(self, NAME):
		return self.__fileName
		
	@fileName.setter
	def fileName(self, NAME):
		if isinstance(NAME, str) and not isinstance(NAME, bool):
			self.__fileName = NAME
		else:
			self.__fileName = -1
		return self.__fileName
		
	@property
	def fileTag(self, TAG):
		return self.__fileTag
		
	@fileTag.setter
	def fileTag(self, TAG):
		if isinstance(TAG, str) and not isinstance(TAG, bool):
			self.__fileTag = TAG
		else:
			self.__fileTag = -1
		return self.__fileTag
		
	@property
	def reqURL(self, URL):
		return self.__reqURL
		
	@reqURL.setter
	def reqURL(self, URL):
		if isinstance(URL, str) and not isinstance(URL, bool):
			self.__reqURL = URL
		else:
			self.__reqURL = -1
		return self.__reqURL
		
	@property
	def request(self, REQUEST):
		return self.__request
		
	@request.setter
	def request(self, REQUEST):
		if isinstance(REQUEST, str) and not isinstance(REQUEST, bool):
			self.__request = REQUEST
		else:
			self.__request = -1
		return self.__request

''' Getter and Setter of Uploading File '''
	@property
	def uploadURL(self, URL):
		return self.__uploadURL
		
	@uploadURL.setter
	def uploadURL(self, URL):
		if isinstance(URL, str) and not isinstance(URL, bool):
			self.__uploadURL = URL
		else:
			self.__uploadURL = -1
		return self.__uploadURL
		
	@property
	def uploadFields(self, FIELDS):
		return self.__uploadFields
		
	@uploadFields.setter
	def uploadFields(self, FIELDS):
		if isinstance(FIELDS, dict) and not isinstance(FIELDS, bool):
			self.__uploadFields = FIELDS
		else:
			self.__uploadFields = -1
		return self.__uploadFields
		
	@property
	def uploadFiles(self, FILES):
		return self.__uploadFiles
		
	@uploadFiles.setter
	def uploadFiles(self, FILES):
		if isinstance(FILES, dict) and not isinstance(FILES, bool):
			self.__uploadFiles = FILES
		else:
			self.__uploadFiles = -1
		return self.__uploadFiles

#-----------------------------------------------------------------------
	def initAuth(self, clientID, authParameters, regionName):
		provider_client = client('cognito-idp', region_name=regionName)
		resp = provider_client.initiate_auth(AuthFlow='USER_PASSWORD_AUTH', 
			AuthParameters=authParameters, ClientId=clientID)
		self.response = resp
		return resp
		
	def getURL(self, response, requestURL):
		access_token = Response["AuthenticationResult"]["IdToken"]
		req = requests.get(RequestURL, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(access_token) })
		self.request = req.json()
		return req
		
	def uploadFile(self, uploadURL, files, fields):
		post = requests.post(uploadURL, files=files, data=fields)
		return post
		
	def setPath(self, path):
		self.uploadFile = {'file': open(f'/home/pi/Desktop/{filename}','rb')}
		
if __name__ == '__main__':
	print('Unit Testing')
	
	path = 
	
	pytest = ER_CloudUpload()
	pytest.clientID = '4vouvmuus59a0imasgo8rcu4b1'
	pytest.authData = {'USERNAME':'testbci01', 
						'PASSWORD':'12345678'}
	pytest.regionName = 'ap-southeast-1'
	
	pytest.fileName = 'ER_CloudUpload_Test.txt'
	pytest.fileTag = 'ER_Test01'
	pytest.reqURL = f'https://83mcanxyj6.execute-api.ap-southeast-1.amazonaws.com/prod-pracha/files/upload-endpoint?fileName={pytest.__fileName}&fileTag={self.__fileTag}'
	
	pytest.initAuth(pytest.clientID, pytest.authData, pytest.regionName)
	pytest.getURL(pytest.response, pytest.reqURL)
	
	pytest.uploadFile(pytest.uploadURL, pytest.uploadFiles, pytest.uploadFields)
		
		
