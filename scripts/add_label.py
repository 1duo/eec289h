#!usr/bin/python

"""
file: add_label.py - add label to feature vector files
input: class_list  - contains all scene categories
  valid_class_file - which need to label to +1
output: class_name - contains all labeled scene feature vectors
  (+1 for the valid category and -1 for all rest)
"""

import fileinput
import sys

# check command line arguments
if (len(sys.argv)) != 4:
    print 'Usage: \npython add_label.py class_list valid_class_file output_file'
    sys.exit()

# output file
out = open (sys.argv[3], 'w')

# read in class_file_list to mark +1 and bring to head
for line_a in fileinput.FileInput(sys.argv[1]):
    line_a = line_a.split()
    length = len(line_a)

    # add label +1 to valid_class
    for i in range (0, length):
        line_a[i] = line_a[i] + '.l2'

        if line_a[i] == sys.argv[2]:
            for sub_line_a in fileinput.FileInput(line_a[i]):
                out.write ('+1 ' + sub_line_a)

        # ignore rest
        else:
            pass

# close class_file_list
fileinput.close()

# read in class_file_list for marking -1 to rest
for line_b in fileinput.FileInput(sys.argv[1]):
    line_b = line_b.split()
    length = len(line_b)

    # add label -1 to rest
    for i in range (0, length):
        line_b[i] = line_b[i] + '.l2'

        if line_b[i] != sys.argv[2]:
            for sub_line_b in fileinput.FileInput(line_b[i]):
                out.write ('-1 ' + sub_line_b)

        # ignore valid class
        else:
            pass

# done
fileinput.close()
out.close()
print 'mission complete: ' + sys.argv[2]
