#! /usr/bin/env python

from sys import argv
import argparse
import matplotlib.pyplot as plt
import os.path


    
if __name__ == "__main__":
    
    original_file = argv[1]
    
    transformer = CurvedLinesTransformer(original_file)
    
    # Do the transform
    print('Running...')
    transformed = transformer.run()
    print('Done!')
            
            
    # Output the final png        
    dot_index = file.rfind('.')
    output_name = file[0:dot_index] + '_output.png'
    scipy.misc.imsave(output_name,transformed)
    
    
    # Display the png
    transformed_render = plt.imshow(transformed)
    plt.gray()
    plt.show(transformed_render)
    
