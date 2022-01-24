from tkinter import image_names
from tracemalloc import Snapshot
import cv2
import dropbox
import time
import random

start_time  = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame  = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "iQZWvMQdK9wAAAAAAAAAAQAlE9_3BHuJGxPAv5G8t4nY4mQIF8O0EC2BMXiFv1nT"
    file = img_name
    file_from = file
    file_to = "/New_Folder_1/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")



def main():
    while(True):
        # if((time.time()-start_time)>=300):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()