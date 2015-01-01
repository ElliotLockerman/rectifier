# Rectifier

For more information, see the [project page](http://elliot.lockerman.info/?page=projects/ergonomic_paper/)

## Introduction

The forearm and hand naturally move in an arc around the elbow. Why then, do we write on straight lines? If it is because text on straight lines is easier to read, computers provide a solution. I present a system for writing on curved lines, offering the potential for advantages in speed, accuracy, and comfort. Copying may particularly benefit, as visual feedback is not required for line tracking.

## The System

Currently a proof of concept, the system is composed of two parts: paper with curved lines on which to write, and software to flatten the lines for reading.

The current paper is composed of 7.213 inch circle segments centered on 8.5 by 11 inch paper. Scanning must be done at 300 dpi.

The software is a command-line program written in Python. Scipy, Numpy, and PIL (or the currently-maintained fork Pillow) are required.

Future versions will allow for more flexibility in paper size, line size and spacing and scanning resolution.


## Software Usage

rectifier.py [-h] [--output] [--overwrite] [-e] input  
  
* positional arguments 
	* input: the document (8.5 by 11 in page, 7.213 in radius circles, 300 dpi) to be rectified, as one of the following image formats: BMP, EPS, GIF, IM, JPEG, JPEG 2000, MSP, PCX, PNG, PPM, SPIDER, TIFF, WebP, XBM, XV Thumbnails, DCX, or FPX  
  
* optional arguments
	* -h, --help: show this help message and exit
	* --output: Set output path/filename. When not set, output is same as input, with '_output' appended before the extension. If --overwrite is not set and the file already exists, '_n' will be appended, where n is the lowest positive integer such that the resulting filename does not yet exist. Note that format/extension is set separately, with '-e'
	* --overwrite: overwrite any previous output files
	* -e, --extension: set the output extension (including the period) of one of the following formats: BMP, EPS, GIF, IM, JPEG, JPEG 2000, MSP, PCX, PNG, PPM, SPIDER, TIFF, WebP, XBM, XV Thumbnails, DCX, FPX, or PDF. The default output format is the same as the input format
