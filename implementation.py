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

#creating 1D gaussian kernels

#notice that there is no denominator term
#normalization will occur within the actual gaussian functions
def modified_gaussian_formula(x,half_width, sigma):
    num = exp(-1 * pow(x - half_width,2)/(2 * pow(sigma,2)))
    return num


sigma = sqrt(2) #for now, we will assign sigma = sqrt(2)
def horizontal_gaussian(img, kernel_width = 3, sigma = sigma):
    img_width,img_height,channels = img.shape
    half_kernel_width = (kernel_width - 1)/2
    print(half_kernel_width)
    sum = 0
    for k in range(0, channels):
        for j in range(0, img_height):
            for i in range(0, img_width):
                img[i][j][k] = modified_gaussian_formula(i, half_kernel_width, sigma) 
                sum += img[i][j][k]
        for j in range(0, img_height):
            for i in range(0, img_width):
                img[i][j][k] = img[i][j][k]/sum
    return img

def vertical_gaussian(img, kernel_width = 3, sigma = sigma):
    img_width,img_height,channels = img.shape
    half_kernel_width = (kernel_width - 1)/2
    print(half_kernel_width)
    sum = 0
    for k in range(0, channels):
        for i in range(0, img_width): 
            for j in range(0, img_height):
                img[i][j] = modified_gaussian_formula(j, half_kernel_width, sigma)
                sum += img[i][j][k]
        for i in range(0, img_width):
            for j in range(0, img_height):
                img[i][j][k] = img[i][j][k]/sum
    return img