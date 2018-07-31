import os
import json

repos = {}
filenames = []

# Walk through each one of the directories and build a hashmap of 
# { dir_name : ['each', 'file', 'in', 'dir']

for i in os.walk('./azure-quickstart-templates').next()[1]:
	repos[i] = os.listdir('./azure-quickstart-templates/' + str(i))
	filenames.append(os.listdir('./azure-quickstart-templates/' + str(i)))

# Obtain all unique files in repos
unique_files = set([item for sublist in filenames for item in sublist])


