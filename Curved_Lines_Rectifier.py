#! /usr/bin/env python

from sys import argv
import scipy.ndimage
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import math




def mapping(output_coords):
    

    input_coords = (output_coords[0] + (-1 * (math.sqrt(2164 ** 2 - (output_coords[1] - 1275) ** 2) - 2164)),output_coords[1],output_coords[2])
        
    return(input_coords)



if __name__ == "__main__" :
    file = argv[1]
    original = scipy.ndimage.imread(file)
    
    test = "test_variable"      
    
    transformed = scipy.ndimage.interpolation.geometric_transform(original, mapping)
            
            
    dot_index = file.rfind('.')
    output_name = file[0:dot_index - 1] + '_output.png'
    scipy.misc.imsave(output_name,transformed)
    
    transformed_render = plt.imshow(transformed)
    plt.gray()
    plt.show(transformed_render)