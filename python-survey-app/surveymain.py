"""
Main survey script. Required submodules will be imported here and file names where the submodules are created
will be named for the ticket detailing the requirement as per requirements.txt. 


"""
from datetime import datetime
import os
# is boto3 available?
import boto3

cwd = os.getcwd()
cwd1 = cwd

if cwd == "/root":
    os.chdir("/root/code")
    cwd = os.getcwd()
    
fnamei = cwd  + '/results.csv'
fnameo = cwd  + '/clean_results.csv'
# os.chdir('./python-survey-app/')
# cwd = os.getcwd()

for currentpath, folders, files in os.walk('.'):
    print(currentpath, folders, files)
    print('')

print(f"{datetime.now()}: surveymain started using {fnamei} as input and {fnameo} as output, cwd {cwd}, was {cwd1}")

from ticket1 import getfile;
from ticket2 import rm_dups;
from ticket3 import ignore_empty;
from ticket4 import capitalise_names;
from ticket5 import rm_out_of_bounds;
from ticket6 import output_file;

# call the getfile function to build the array from the input file
# lines = getfile('c:\Users\MalcBackup\OneDrive\Documents\GitHub\-multiverse-devops-assessment-2\python-survey-app\results.csv')
# lines = getfile('./results.csv')
print(f"{datetime.now()}: getfile")
lines = getfile(fnamei)


# print the array line by line
# print(*lines)

print(f"{datetime.now()}: ignore_empty")
lines = ignore_empty(lines)

# print the array line by line
# print(*lines)

print(f"{datetime.now()}: rm_dups")
lines = rm_dups(lines)

# print the array line by line
# print(*lines)

print(f"{datetime.now()}: capitalise_names")
lines = capitalise_names(lines)

# print the array line by line
# print(*lines)

print(f"{datetime.now()}: rm_out_of_bounds")
lines = rm_out_of_bounds(lines)

# print the array line by line
# print(*lines)

# write out the clean results
print(f"{datetime.now()}: output_file")
output_file(fnameo,lines)
print('')
for currentpath, folders, files in os.walk('.'):
    print(currentpath, folders, files)
    print('')

print('')

print(f"{datetime.now()}: surveymain completed using {fnamei} as input and {fnameo} as output")

