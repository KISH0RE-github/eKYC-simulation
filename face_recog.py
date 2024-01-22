import dlib, cv2,os
import matplotlib.pyplot as plt
import numpy as np
from imutils.face_utils import FaceAligner
from PIL import Image
from scipy.spatial.distance import euclidean
import FaceReco.FaceReco as fr
import face_recognition

def read_img(path):
    img=cv2.imread(path)
    (h,w)=img.shape[:2]
    width=500
    ratio=width/float(w)
    height=int(h*ratio)
    return cv2.resize(img,(width,height))


print("Plese Enter your customer id. given by the bank:\n") 
cus_no=int(input())  #from website
appl_photo_encoding=[]
appl_no=[]
addr="directory of folders containing application photo and captures folders"
for file in os.listdir("directory of folders containing application photo folder"): #Going through all photos in application form folder
    if file.endswith(".png"):
        appl_addr=addr+"\\application photo\\"+file
        img1=read_img(appl_addr)
        cv2.imshow("picture",img1)
        cv2.waitKey(1000)
        img1_enc=face_recognition.face_encodings(img1)[0]
        appl_photo_encoding.append(img1_enc)
        appl_no.append(file.split('.')[0])
        print(appl_addr)
    

captr_addr=addr+"\\captures\\"+str(cus_no)+".png" #Address of photo requested customer
img2=read_img(captr_addr)
img2_enc=face_recognition.face_encodings(img2)[0]
print(captr_addr)
print("The encoding of captures image:\n\n")
print(img2_enc)
result=face_recognition.compare_faces(appl_photo_encoding,img2_enc)

count=0
for i in range(len(result)):
    if result[i]==True:
        print("\n\nThe captured image matches with: "+appl_no[i])
        count+=1
if(count==0):
    print("The face doesnt match with any photo from application forms")
print(result)
