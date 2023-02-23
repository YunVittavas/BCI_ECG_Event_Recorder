import os
import pandas as pd
import time

class ER_UpdateParam():
	def __init__(self):
		self.unixTimestamp = time.time()
		
	def readCSV(self, files):
		files = pd.read_csv(files)
		return files
		
if __name__ == '__main__':
	param = ER_UpdateParam()
	print(param.unixTimestamp)
	
