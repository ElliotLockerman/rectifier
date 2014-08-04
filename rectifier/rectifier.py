#! /usr/bin/env python

import sys
import os.path
import argparse
from morph import Transformer
import utils
import matplotlib.pyplot as plt
import scipy

    
if __name__ == "__main__":
    
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the document to be rectified, as one of the following image formats: BMP, EPS, GIF, IM, JPEG, JPEG 2000, MSP, PCX, PNG, PPM, SPIDER, TIFF, WebP, XBM, XV Thumbnails, DCX, or FPX")
    parser.add_argument("--output", help="Set output path/filename. Default is same as input, with '_output' appended. If --overwrite is not set and the file already exists '_n' will be appended, where n is the lowest number that can be added such that the resulting filename does not exist")
    parser.add_argument("--overwrite", help="overwrite any previous output files", action="store_true")
    parser.add_argument("-e", "--extension", help="set output extension to one of the following formats: BMP, EPS, GIF, IM, JPEG, JPEG 2000, MSP, PCX, PNG, PPM, SPIDER, TIFF, WebP, XBM, XV Thumbnails, DCX, FPX, or PDF. The default output format is the same as the input format")
    
    # Parse arguments
    args = parser.parse_args()
    original_file_path = args.input
    output_file_path = args.output
    overwrite = args.overwrite
    
    if args.extension:
        output_format = args.extension
        
        if output_format[0] != '.':
            sys.stderr.write("Error: output format must be specified as an extension")
            print("")
            sys.exit(1)
            
    else:
        x,args.format = os.path.splitext(original_file_path) # If the argument wasn't set, the default is the same as the origonal
    
    
    # Do the transform
    print('Running...')
    transformer = Transformer(original_file_path)
    transformed = transformer.run()
    print('Done!')
            
            
    # Output the final png
    if not output_file_path:
        output_file_path = utils.generate_output_file_path(original_file_path, overwrite, output_format)
    elif os.path.exists(output_file_path) and not overwrite:
        output_file_path = utils.find_earliest_output_path(output_file_path)
    scipy.misc.imsave(output_file_path,transformed)
    print("Saved to: " + output_file_path)
    
    
    # Display the png
    transformed_render = plt.imshow(transformed)
    plt.gray()
    plt.show(transformed_render)
    
