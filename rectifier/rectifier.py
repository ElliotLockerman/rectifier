#! /usr/bin/env python

import sys
import os.path
import argparse
import matplotlib.pyplot as plt
import scipy
import scipy.ndimage
from math import sqrt


    
    
    
# Functions for file name generation    
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
    i = 1
        
    if not os.path.exists(output_file_path):
        earliest_output_path_found = True    
        new_output_file_path = output_file_path
        
    # Look through numbers to append untill the one thats not used is found
    while earliest_output_path_found == False:
        dot_index = output_file_path.rfind('.')
        new_output_file_path = output_file_path[:dot_index] + '_' + str(i) + output_file_path[dot_index:]
        
        i = i + 1
        
        if not os.path.exists(new_output_file_path):
            earliest_output_path_found = True
            
    return new_output_file_path
    





# Does the transformation. 
class Transformer:
    
    def __init__(self, original_file_path):

        # Load up the image
        self.original_image = scipy.ndimage.imread(original_file_path)    
        
        # Set up measurments
        self.original_width_pixels = self.original_image.shape[1]
        self.circle_radius_inches = 7.213
        self.pixels_per_inch = 300
        self.circle_radius_pixels = 7.213 * self.pixels_per_inch
        
        self.max_vertical_offset = (-1 * (sqrt(self.circle_radius_pixels ** 2 - (0 - (self.original_width_pixels / 2)) ** 2) - self.circle_radius_pixels))

        self.output_shape_list = list(self.original_image.shape)
        self.output_shape_list[0] = int(round(self.original_image.shape[0] + self.max_vertical_offset))
        self.output_shape = tuple(self.output_shape_list)

    
    def run(self):
        return scipy.ndimage.interpolation.geometric_transform(input=self.original_image, mapping=self.mapping, output_shape=self.output_shape, mode="constant", cval=255)


    def mapping(self, output_coords):

        input_coords = (output_coords[0] + (-1 * (sqrt(self.circle_radius_pixels ** 2 - (output_coords[1] - (self.original_width_pixels / 2)) ** 2) - self.circle_radius_pixels + self.max_vertical_offset)), output_coords[1])

        # For color images, there are extra dimensions; we don't need to shift the colors, so give 'em back what they gave us.
        if len(output_coords) == 3:
            input_coords = input_coords + (output_coords[2],)
        elif len(output_coords) == 4:
            input_coords = input_coords + (output_coords[3],)
    
        return(input_coords)
        


# The main program 
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
        output_file_path_final = generate_output_file_path(original_file_path_argument, overwrite_argument, output_format)
    elif os.path.exists(output_file_path_argument) and not overwrite_argument:
        output_file_path_final = find_earliest_output_path(output_file_path_argument)
    else:
        output_file_path_final = output_file_path_argument
    
    scipy.misc.imsave(output_file_path_final, transformed)
    print("Saved to: " + output_file_path_final)
    
    
    # Display the png
    transformed_render = plt.imshow(transformed)
    plt.gray()
    plt.show(transformed_render)
    