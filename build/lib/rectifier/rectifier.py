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
    parser.add_argument("input", help="the document (8.5 by 11 in page, 7.213 in radius circles, 300 dpi) to be rectified, as one of the following image formats: BMP, EPS, GIF, IM, JPEG, JPEG 2000, MSP, PCX, PNG, PPM, SPIDER, TIFF, WebP, XBM, XV Thumbnails, DCX, or FPX")
    parser.add_argument("--output", help="Set output path/filename. When not set, output is same as input, with '_output' appended before the extension. If --overwrite is not set and the file already exists, '_n' will be appended, where n is the lowest positive integer such that the resulting filename does not yet exist. Note that format/extension is set separately, with '-e'")
    parser.add_argument("--overwrite", help="overwrite any previous output files with the same name", action="store_true")
    parser.add_argument("-e", "--extension", help="set the output extension (including the period) of one of the following formats: BMP, EPS, GIF, IM, JPEG, JPEG 2000, MSP, PCX, PNG, PPM, SPIDER, TIFF, WebP, XBM, XV Thumbnails, DCX, FPX, or PDF. The default output format is the same as the input format") # Setting the extension/format separately allows one to change the format but keep the default (input based) output name
    
    # Parse arguments
    args = parser.parse_args()
    original_file_path_argument = args.input
    output_file_path_argument = args.output
    overwrite_argument = args.overwrite
    extension_argument = args.extension
    
    if extension_argument:
        output_format = extension_argument
        
        if output_format[0] != '.':
            sys.stderr.write("Error: output format must be specified as an extension, not a format name (and the first character must be a period).")
            print("")
            sys.exit(1)
            
    else:
        x, output_format = os.path.splitext(original_file_path_argument) # If the argument wasn't set, the default is the same as the origonal
    
    
    # Do the transform
    print('Running...')
    transformer = Transformer(original_file_path_argument)
    transformed = transformer.run()
    print('Done!')
            
            
    # Output the final png
    if not output_file_path_argument:
        output_file_path_final = utils.generate_output_file_path(original_file_path_argument, overwrite_argument, output_format)
    elif os.path.exists(output_file_path_argument) and not overwrite_argument:
        output_file_path_final = utils.find_earliest_output_path(output_file_path_argument)
    else:
        output_file_path_final = output_file_path_argument
    
    scipy.misc.imsave(output_file_path_final, transformed)
    print("Saved to: " + output_file_path_final)
    
    
    # Display the png
    transformed_render = plt.imshow(transformed)
    plt.gray()
    plt.show(transformed_render)
    
