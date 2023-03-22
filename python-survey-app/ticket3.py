'''
3: Ignore empty lines
Description:
    Update your input script to ignore any empty lines found when reading in the input data file
Objectives:
    ●	 A final array is created with any empty lines omitted.
'''
def ignore_empty(filecontent:list):
    out_list = []
    for l in filecontent:
    # drop blanks
        if l[0] != ',':
            out_list.append(l)

    return out_list
