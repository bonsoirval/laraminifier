from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import re

file_path = 'about.blade.php' #file to be optimised

def replace(file_path):#, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                line = ' '.join(line.split()) #remove all whitespaces from the html file line
                line = re.sub(r"<!--(.|\s|\n)*?-->", "", line) #remove all html comment
                new_file.write(line) #write / save the lines to the file
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)
replace(file_path)
