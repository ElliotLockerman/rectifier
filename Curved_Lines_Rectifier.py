#! /usr/bin/env python

from sys import argv
import scipy.ndimage
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import math




def mapping(output_coords):
    

    input_coords = (output_coords[0] + (-1 * (math.sqrt(circle_radius_pixels ** 2 - (output_coords[1] - (original_width_pixels / 2)) ** 2) - circle_radius_pixels)), output_coords[1], output_coords[2])
        
    return(input_coords)



if __name__ == "__main__" :
    
    # Load up the image
    file = argv[1]
    original_image = scipy.ndimage.imread(file)    

    # Set up measurments
    paper_width_inches = 8.5
    circle_radius_inches = 7.213
    original_width_pixels = original_image.shape[1]
    pixels_per_inch = original_width_pixels / paper_width_inches
    circle_radius_pixels = 7.213 * pixels_per_inch
    
    
    # Do the transform
    print('Running...')
    transformed = scipy.ndimage.interpolation.geometric_transform(original_image, mapping)
    print('Done!')
            
    # Output the final png        
    dot_index = file.rfind('.')
    output_name = file[0:dot_index - 1] + '_output.png'
    scipy.misc.imsave(output_name,transformed)

    
    # Display the png
    transformed_render = plt.imshow(transformed)
    plt.gray()
    plt.show(transformed_render)