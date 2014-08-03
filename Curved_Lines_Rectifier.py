#! /usr/bin/env python

from sys import argv
import scipy.ndimage
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import math






class Curved_Lines_Rectifier:
    
    def __init__(self):

        # Load up the image
        file = argv[1]
        original_image = scipy.ndimage.imread(file)    
        
        # Set up measurments
        self.original_width_pixels = original_image.shape[1]
        self.circle_radius_inches = 7.213
        self.pixels_per_inch = 300
        self.circle_radius_pixels = 7.213 * self.pixels_per_inch
        
        
        # Do the transform
        print('Running...')
        transformed = scipy.ndimage.interpolation.geometric_transform(original_image, self.mapping)
        print('Done!')
                
                
        # Output the final png        
        dot_index = file.rfind('.')
        output_name = file[0:dot_index] + '_output.png'
        scipy.misc.imsave(output_name,transformed)
        
        
        # Display the png
        transformed_render = plt.imshow(transformed)
        plt.gray()
        plt.show(transformed_render)
    
    


    def mapping(self, output_coords):

        input_coords = (output_coords[0] + (-1 * (math.sqrt(self.circle_radius_pixels ** 2 - (output_coords[1] - (self.original_width_pixels / 2)) ** 2) - self.circle_radius_pixels)), output_coords[1])

        # For color images, there are extra dimensions; we don't need to shift, 
        # so give 'em back what they gave us.
        if len(output_coords) == 3:
            input_coords = input_coords + (output_coords[2],)
        elif len(output_coords) == 4:
            input_coords = input_coords + (output_coords[3],)
    
        return(input_coords)
    
    
    
if __name__ == "__main__" :
    rectifier = Curved_Lines_Rectifier()
    
    