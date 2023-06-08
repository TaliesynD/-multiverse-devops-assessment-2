'''
7: Create an output script
Description:
    A new output script will be created which reads in the clean_results.csv CSV file and outputs the results to the command line, row by row
Objectives:
	●	 The script uses the existing sub-module to read the CSV file.
	●	 The printed output will contain all row data and an appropriate header.
	●	 Stretch: The printed output will be formatted with fixed length strings.
'''

import os
from datetime import datetime

fnamei = './code/clean_results.csv'

for currentpath, folders, files in os.walk('.'):
    print(currentpath, folders, files)
    print('')

print('')

print(f"{datetime.now()}: surveyout started using {fnamei} as input")

from ticket7 import output_script;
# print the clean file
output_script(fnamei)

print(f"{datetime.now()}: surveyout completed using {fnamei} as input")
