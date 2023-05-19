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
        # force uppercase but not in the header row
        if l.split(',')[0] == 'user_id':
            out_list.append(l)
        else: 
            m = l.split(',')[0] + ',' + l.split(',')[1].capitalize() + ',' +  l.split(',')[2].capitalize() + ',' + l.split(',')[3] + ',' + l.split(',')[4] + ',' + l.split(',')[5]
            out_list.append(m)
       
    return out_list
