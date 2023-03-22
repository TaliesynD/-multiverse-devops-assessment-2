'''
5: Validate the responses to answer 3
Description:
    Update your input script to validate the responses to the third answer field. This answer must have a numeric value between 1 and 10. Any rows with an invalid value are ignored.

Objectives:
	●	 A final array is created with the input data excluding any rows where answer 3 is invalid.
	●	 No answer 3 values will be outside the range of 1 to 10
 
'''

def rm_out_of_bounds(filecontent:list):
    out_list = []
    for l in filecontent:
    # last element needs to be between 1 and 10
        # print(l.split(',')[5])
        if l.split(',')[5] == 'answer_3\n':
            out_list.append(l)
        else: 
            if int(l.split(',')[5]) > 0 and int(l.split(',')[5]) < 11:
                out_list.append(l)
            
    return out_list
