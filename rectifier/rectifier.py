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
    parser.add_argument("--overwrite", help="overwrite any previous output files", action="store_true")
    parser.add_argument("-e", "--extension", help="set output extension to one of the following formats: BMP, EPS, GIF, IM, JPEG, JPEG 2000, MSP, PCX, PNG, PPM, SPIDER, TIFF, WebP, XBM, XV Thumbnails, DCX, FPX, or PDF. The default output format is the same as the input format")
    
    # Parse arguments
    args = parser.parse_args()
    original_file_path = args.input
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
    output_file_path = utils.generate_output_file_path(original_file_path, overwrite, output_format)
    scipy.misc.imsave(output_file_path,transformed)
    print("Saved as: " + output_file_path)
    
    
    # Display the png
    transformed_render = plt.imshow(transformed)
    plt.gray()
    plt.show(transformed_render)
    
