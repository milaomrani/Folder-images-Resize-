from PIL import Image
import os
import cv2
import glob

rootDir = "Source Folder"  #/content/drive/MyDrive
rgb2grayPath = "Destination Folder"

for img in glob.iglob(rootDir + '**/*.jpg', recursive=True):
    print(img)
    im = Image.open(img)
    size = "Insert your size"
    imResize = im.resize((size,size), Image.ANTIALIAS)
    #The image quality, on a scale from 0 (worst) to 95 (best).
    # The default is 75. # Values above 95 should be avoided;
    imResize.save(img, 'JPEG', quality=95)





try:
    makedirs(rgb2grayPath)
except:
    print ("Directory already exist, images will be written in same folder")

# Folder won't used
images = os.listdir(rootDir)

for img in images:
    img = cv2.imread(os.path.join(rootDir,img))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(rgb2grayPath,img),gray)


