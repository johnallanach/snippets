  
""" this short piece of code replaces unwanted text in file names with a new string """

import os


def cleanfiles(text_to_remove, text_to_insert, working_path):
    # running tallies of cleaned/uncleaned files
    cleaned = []
    uncleaned =[]

    # find all files/paths in working path 
    paths = (os.path.join(root, filename)
            for root, _, filenames in os.walk(working_path)
            for filename in filenames)

    # iteratively change file names
    for path in paths:
        try:
            newname = path.replace(text_to_remove, text_to_insert)
            if newname != path:
                os.rename(path, newname)
                cleaned.append(newname)
        except Exception:
            uncleaned.append(newname)
    
    # provide a final tally of cleaned/uncleaned file names
    if len(cleaned) > 0:
        print('Total files cleaned: %s' % str(len(cleaned)))
    if len(uncleaned) > 0:
        print('Total files not cleaned: %s' % str(len(uncleaned)))


if __name__ == '__main__':
    # collect user inputs 
    text_to_remove = input("Text to be removed: ")
    text_to_insert = input("Text to be inserted: (leave blank to remove unwanted text with no replacement) ")
    working_path = 'r' + input("Path of files to be re-named: ")
    
    #execute main code
    cleanfiles(text_to_remove, text_to_insert, working_path)

    # complete task
    print("File name cleaning task complete.")

