from ticket1 import getfile;
from ticket2 import rm_dups;
from ticket3 import ignore_empty;
from ticket4 import capitalise_names;
from ticket5 import rm_out_of_bounds;
from ticket6 import output_file;
from ticket7 import output_script;

import os
cwd = os.getcwd()
fnamei = cwd  + '/results.csv'
fnameo = cwd  + '/clean_results.csv'


# ticket1 - read CSV
def test_getfile():
    assert(isinstance(getfile(fnamei),(str,list)))
    
# ticket 2 - Remove duplicates
def test_rm_dups():
    infile = getfile(fnamei)
    infile = rm_dups(infile)
    prev = ''
    dupfound = 0
    for i in infile:
        if i.split(',')[0]==prev:
            dupfound = 1
    prev = i.split(',')[0]
    assert(dupfound == 0)

# ticket 3 - Ignore empty lines
def test_ignore_empty():
    infile = getfile(fnamei)
    infile2 = ignore_empty(infile)
    assert(',,,,,' not in infile2)
    
# ticket 4 - Capitalise user name fields
def test_capitalise_names():
    infile = getfile(fnamei)
    infile = ignore_empty(infile)
    infile = capitalise_names(infile)
    for l in infile:
        # print('---' + l[1] + '---')
       if l.split(',')[0] != 'user_id':
            m = str(l.split(',')[1]).capitalize()
            n = str(l.split(',')[1])
            assert(n == m)
    
# ticket 5 - Validate the responses to answer 3
def test_rm_out_of_bounds():
    infile = getfile(fnamei)
    infile = ignore_empty(infile)
    infile = rm_out_of_bounds(infile)
    for l in infile:
        if l.split(',')[5] != 'answer_3\n':
            assert(int(l.split(',')[5]) > 0)
            assert(int(l.split(',')[5]) < 11)
        
    
# ticket 6 - Output the cleansed result data to a new file
import os.path
def test_output_file():
    out_line = ['99','a','b','1','2','3']
    output_file(fnameo,out_line)
    assert(os.path.isfile(fnameo))
    
# ticket 7 - Create an output script
def test_output_script():
    # this writes to stdout, so how would we test? Pipe stdout to a file and read the file?
    assert(1==1)
    
# main survey script test
#def test_surveymain():
#    assert(1==1)
