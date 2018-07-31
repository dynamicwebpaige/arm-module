import os
import json

repos = {}

for i in os.walk('./azure-quickstart-templates').next()[1]:
	repos[i] = os.listdir('./azure-quickstart-templates/' + str(i))

print json.dumps(repos)
