import os

os.chdir('D:\\Projects\\BFC\\37. Russia\\1. Sberbank\\GET requests')

region_requests = []

for root, dirs, files in os.walk(".", topdown = True):
	for file_name in files:
		with open(file_name, 'r') as fh:
			GET_request = fh.read()
			
		region_requests.append({
			'region': file_name,
			'GET_request': GET_request
		})

print(region_requests)