'''
4: Capitalise user name fields
Description:
    Add functionality to your input script to automatically capitalise the first_name and last_name fields found in the input data.
Objectives:
    ●	 All names are capitalised in all data entries
    
user_id,first_name,last_name,answer_1,answer_2,answer_3

'''
# I have made a correction to your header column, which stops the 'first name' and 'last name' columns from being capitalized.

# Use this change to continue with your name columns completely capitalized

def capitalise_names(filecontent:list):
    out_list = []
    for i,l in enumerate(filecontent):
        if i < 1:
            out_list.append(l)
        else:
            # force uppercase
            m = l.split(',')[0] + ',' + l.split(',')[1].upper() + ',' +  l.split(',')[2].upper() + ',' + l.split(',')[3] + ',' + l.split(',')[4] + ',' + l.split(',')[5]
            out_list.append(m)
       
    return out_list


# my interpretation was that only the first letter of the names were supposed to be capitalized, in which case use the code commented out below.

# def capitalize_lines(input_list):
#     survey_list = input_list
#     for i in survey_list[1:]:
#         i = i.split(',')
#         i[1] = i[1].capitalize()
#         i[2] = i[2].capitalize()
#         i = str(i)
#     return survey_list