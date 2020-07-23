# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:03:19 2020

@author: prach
"""
# this code writes into csv one column at a time. Run 1: NSE 2: BSE
#run 2 times for outout csv changing read and write object files

from csv import writer
from csv import reader
import random
#default_text = 'Some Text'
# Open the input_file in read mode and output_file in write mode
with open('C:/Users/prach/spyder_workspace/output2.csv', 'r') as read_obj, \
        open('output3.csv', 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
    # Read each row of the input csv file as list
    
    
    for row in csv_reader:
        # Append the default text in the row / list
        row.append(random.randint(1,2000))
        # Add the updated row / list to the output file
        csv_writer.writerow(row)
    
    