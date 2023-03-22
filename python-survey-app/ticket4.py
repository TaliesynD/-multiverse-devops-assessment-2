'''
4: Capitalise user name fields
Description:
    Add functionality to your input script to automatically capitalise the first_name and last_name fields found in the input data.
Objectives:
    ●	 All names are capitalised in all data entries
    
user_id,first_name,last_name,answer_1,answer_2,answer_3

'''
def capitalise_names(filecontent:list):
    out_list = []
    for l in filecontent:
        # force uppercase
        m = l.split(',')[0] + ',' + l.split(',')[1].upper() + ',' +  l.split(',')[2].upper() + ',' + l.split(',')[3] + ',' + l.split(',')[4] + ',' + l.split(',')[5]
        out_list.append(m)
       
    return out_list
