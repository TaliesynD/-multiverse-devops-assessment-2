"""
Main survey script. Required submodules will be imported here and file names where the submodules are created
will be named for the ticket detailing the requirement as per requirements.txt. 


"""
from datetime import datetime
import os

now = datetime.now()
cwd = os.getcwd()
fnamei = cwd  + '/python-survey-app/results.csv'
fnameo = cwd  + '/python-survey-app/clean_results.csv'


print(f"{now}: surveymain started using {fnamei} as input and {fnameo} as output")

from ticket1 import getfile;
from ticket2 import rm_dups;
from ticket3 import ignore_empty;
from ticket4 import capitalise_names;
from ticket5 import rm_out_of_bounds;
from ticket6 import output_file;

# call the getfile function to build the array from the input file
# lines = getfile('c:\Users\MalcBackup\OneDrive\Documents\GitHub\-multiverse-devops-assessment-2\python-survey-app\results.csv')
# lines = getfile('./results.csv')
lines = getfile(fnamei)


# print the array line by line
# print(*lines)

lines = ignore_empty(lines)

# print the array line by line
# print(*lines)

lines = rm_dups(lines)

# print the array line by line
# print(*lines)

lines = capitalise_names(lines)

# print the array line by line
# print(*lines)

lines = rm_out_of_bounds(lines)

# print the array line by line
# print(*lines)

# write out the clean results
output_file(fnameo,lines)

now = datetime.now()
print(f"{now}: surveymain completed using {fnamei} as input and {fnameo} as output")

