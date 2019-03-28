from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import re

file_path = 'about.blade.php' #file to be optimised

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                line = re.sub(r"<!--(.|\s|\n|[ \t]+)*?-->", "", line)
                #line = re.sub(r">(\s+)<", "><", line)
                new_file.write(line.replace(pattern, subst))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)
replace(file_path, '\n','')
#replace(file_path, '', '')
