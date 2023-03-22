'''
7: Create an output script
Description:
    A new output script will be created which reads in the clean_results.csv CSV file and outputs the results
    to the command line, row by row
Objectives:
	●	 The script uses the existing sub-module to read the CSV file.
	●	 The printed output will contain all row data and an appropriate header.
	●	 Stretch: The printed output will be formatted with fixed length strings.

'''
from ticket1 import getfile

def output_script(fn:str):
    f = getfile(fn)
    for i in f:
        print(f"{i.split(',')[0]:>3}" + "," + f"{i.split(',')[1]:<20}" + "," + f"{i.split(',')[2]:<20}" + "," + f"{i.split(',')[3]:<3}" + "," + f"{i.split(',')[4]:<1}" + "," + f"{i.split(',')[5]:<2}".rstrip())


        