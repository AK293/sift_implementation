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
seed_img = cv2.GaussianBlur(bilinear_img, (0,0), seed_sigma/sqrt(2), cv2.BORDER_DEFAULT)

def sigma_formula(octave, scale):
    return sigma_min/interpixel_min * sqrt(pow(2, 2*scale/spo) - pow(2, 2*(scale-1)/spo))
def new_interpixel_value(octave):
    return interpixel_min * exp(2, octave-1)

curr_img = seed_img[:]
plt.imshow(seed_img,cmap = 'gray')
plt.title('Octave 1, Scale 0: Seed Image'.format()), plt.xticks([]), plt.yticks([])
plt.show()

images = {} #keys are two-digit nummbers: 
                #1st digit = octave #, 2nd digit = scale #
                #values are images
images[10] = seed_img

for i in range(1, spo + 3):
    sigma_value = sigma_formula(1, i)
    images[10+i] = cv2.GaussianBlur(curr_img, (0,0), sigma_value, cv2.BORDER_DEFAULT)
    curr_img = images[10+i]

for j in range(2, oct_max + 1):
    width, height = curr_img.shape[1] // 2, curr_img.shape[0] // 2
    dim = (width, height)
    images[j*10] = cv2.resize(curr_img, dim)  
    curr_img = images[j*10]    
    for i in range(1, spo+3):
        sigma_value = sigma_formula(j, i)   
        images[j*10+i] = cv2.GaussianBlur(curr_img, (0,0), sigma_value, cv2.BORDER_DEFAULT)
        curr_img = images[j*10+1]

#Difference of Gaussians
"""
Keys are two-digit numbers. 1st digit = octave
#2nd digit = lower ones digit
#i.e. the DOG between scale 2 and scale 1 for octave 6 will have a key of 61.
"""
dog = {}
for octave in range(1, oct_max+1):
    for scale in range(0, spo+2):
        dog[octave*10+scale] = images[octave*10+scale+1] - images[octave*10+scale]