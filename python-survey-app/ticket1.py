def getfile(fn:str):
    # create empty array for lines from input file
    lines_array = []
    
    # open the file, then iterate over it building the array
    
    f = open(fn,'rt')

    for line in f:
            lines_array.append(line)
    
    f.close()
    
    return lines_array
