'''
2: Remove duplicate entries
Description:
    Add functionality to your input script to ignore or remove any duplicate entries from the input data. Duplicates are based on the User Id field.
Objectives:
    ●	 A final array is created with duplicate entries removed.
    ●	 Where duplicates are found, the first entry is retained.
'''
def rm_dups(filecontent:list):
    out_list = []
    id_list = []
    for l in filecontent:
    # if the id doesn't already exist, we need this record, otherwise skip
        if l.split(',')[0] != '' and l.split(',')[0] not in id_list:
            id_list.append(l.split(',')[0])
            out_list.append(l)
            
    return out_list
