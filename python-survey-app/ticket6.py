'''
6: Output the cleansed result data to a new file
Description:
    Add functionality to your input script to output the cleansed data to a new CSV file.
Objectives:
	●	 A new file is created called clean_results.csv.
	●	 The file is recreated on each execution.
	●	 No invalid or unformatted data is present in the new file.

'''
def output_file(fn:str,indata:list):
    f = open(fn,'w')

    for line in indata:
        f.write(line)
    f.close()
    