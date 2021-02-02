import cv2
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt, pow, pi, exp

img = cv2.imread('eiffel_tower.JPG')
dimensions = img.shape
print('Image Dimensions:',dimensions)

#Defining the default parameter values
k = sqrt(2)
oct_max = 8 #number of octaves
spo = 3 #scales per octave
sigma_input = 0.5
sigma_min = 0.8

bilinear_img = cv2.resize(img,None, fx = sqrt(2), fy = sqrt(2), interpolation = cv2.INTER_LINEAR)
seed_sigma = 1/sigma_min* sqrt(pow(sigma_min,2)-pow(sigma_input,2))

def gaussian_formula(x,y,sigma):
    x_bar = sqrt(pow(x,2) + pow(y, 2))
    num = exp(-1 * pow(x_bar,2)/(2 * pow(sigma,2)))
    denom = 2 * pi * pow(sigma,2)
    return num/denom

for i in range(1, oct_max):
    interpixel_distance = pixel_min * pow(2,i-1)
    sigma_first_part = interpixel_distance/interpixel_min * sigma_min
    for j in range(1:spo + 2):
        sigma = sigma * pow(2, j/spo)