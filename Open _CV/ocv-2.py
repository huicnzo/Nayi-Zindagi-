##Reading an image##



# Importing the OpenCV library 
import cv2 
# Reading the image using imread() function 
image = cv2.imread('image.png') 

# Extracting the height and width of an image 
h, w = image.shape[:2]  #########mahiiiemaaaa , isn't here so its definitely not for matrix but for array !!!!!  


####This is a combination of slicing and sequence unpacking. The colon isn't a wildcard; it denotes a range, or more precisely a slice of the array's indices. It's meant to be intuitive and the syntax is start:stop:step, where if omitted they default to 0, the end of the list, and 1, respectively. See the docs for more details. 
#So here it's saying to take the first two elements of the shape attribute.

#Sequence unpacking just means that if you have a sequence of length N on the right hand side of an assignment, 
#you can unpack it and assign it into N valid names on the left-hand side. So if you know that shape is (height × width × other dimensions) 
#then you can grab just height and width by taking the first two elements, [:2], and unpacking them appropriately.



# Displaying the height and width 
print("Height = {}, Width = {}".format(h, w)) 



###Extracting the RGB values of a  individual pixel

# Extracting RGB values. 
# Here we have randomly chosen a pixel 
# by passing in 100, 100 for height and width. 
(B, G, R) = image[100, 100]  ## this value will be filled on its own .here 100 , 100 only means we are passing the values of height & weight .

# Displaying the pixel values 
print("R = {}, G = {}, B = {}".format(R, G, B)) 

# We can also pass the channel to extract 
# the value for a specific channel 
B = image[100, 100, 0] 
print("B = {}".format(B)) 

##Region of Interest 

# We will calculate the region of interest 
# by slicing the pixels of the image 
roi = image[100 : 500, 200 : 700]  #2d matrix  

#do remember image itself is a parameter

## Resizing Image

# resize() function takes 2 parameters, 
# the image and the dimensions 
resize = cv2.resize(image, (800, 800)
                   
                   #above we have only changed the width soo....
 ##The problem with this approach is that the aspect ratio of the image is not maintained. 
  #So we need to do some extra work in order to maintain a proper aspect ratio.

  # Calculating the ratio 
ratio = 800 / w 

# Creating a tuple containing width and height 
dim = (800, int(h * ratio)) 

# Resizing the image 
resize_aspect = cv2.resize(image, dim) 

                    
##Rotating The Image
                    
 # Calculating the center of the image 
center = (w // 2, h // 2) 
  
# Generating a rotation matrix 
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)  
  
# Performing the affine transformation 
rotated = cv2.warpAffine(image, matrix, (w, h))
                    
 

