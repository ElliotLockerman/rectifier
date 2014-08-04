#!/usr/bin/env python

import os.path


def generate_output_file_path(original_file_path, overwrite, output_format):
    
    dot_index = original_file_path.rfind('.')
    output_file_path = original_file_path[0:dot_index] + '_output' + output_format
                       
    if not os.path.isfile(output_file_path) or overwrite == True:
        return output_file_path
    else:
        output_file_path = find_earliest_output_path(output_file_path)
        return output_file_path

        
def find_earliest_output_path(output_file_path):
    
    earliest_output_path_found = False
    i = 2
        
    
    while earliest_output_path_found == False:
        dot_index = output_file_path.rfind('.')
        new_output_file_path = output_file_path[:dot_index] + '_' + str(i) + output_file_path[dot_index:]
        
        i = i + 1
        
        if not os.path.exists(new_output_file_path):
            earliest_output_path_found = True
            
    return new_output_file_path
    
