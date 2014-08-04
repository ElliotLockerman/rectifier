#! /usr/bin/env python


import scipy.ndimage
from math import sqrt


class Transformer:
    
    def __init__(self, original_file_path):

        # Load up the image
        self.original_image = scipy.ndimage.imread(original_file_path)    
        
        # Set up measurments
        self.original_width_pixels = self.original_image.shape[1]
        self.circle_radius_inches = 7.213
        self.pixels_per_inch = 300
        self.circle_radius_pixels = 7.213 * self.pixels_per_inch
        

    
    def run(self):
        return scipy.ndimage.interpolation.geometric_transform(self.original_image, self.mapping)


    def mapping(self, output_coords):

        input_coords = (output_coords[0] + (-1 * (sqrt(self.circle_radius_pixels ** 2 - (output_coords[1] - (self.original_width_pixels / 2)) ** 2) - self.circle_radius_pixels)), output_coords[1])

        # For color images, there are extra dimensions; we don't need to shift the colors, so give 'em back what they gave us.
        if len(output_coords) == 3:
            input_coords = input_coords + (output_coords[2],)
        elif len(output_coords) == 4:
            input_coords = input_coords + (output_coords[3],)
    
        return(input_coords)
    