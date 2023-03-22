"""
Main survey script. Required submodules will be imported here and file names where the submodules are created
will be named for the ticket detailing the requirement as per requirements.txt. 


"""


from ticket1 import getfile;
from ticket2 import rm_dups;
from ticket3 import ignore_empty;
from ticket4 import capitalise_names;
from ticket5 import rm_out_of_bounds;
from ticket6 import output_file;
from ticket7 import output_script;

# call the getfile function to build the array from the input file
# lines = getfile('c:\Users\MalcBackup\OneDrive\Documents\GitHub\-multiverse-devops-assessment-2\python-survey-app\inputfile.csv')
lines = getfile('python-survey-app/inputfile.csv')

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
output_file('python-survey-app/clean_results.csv',lines)

# print the clean file
output_script('python-survey-app/clean_results.csv')
