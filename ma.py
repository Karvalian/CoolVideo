# ~-~- Written and maintained by Karvalian.
# ~-~- frame by frame feature updates 2 frames per key.
# ~-~- automatic feature plays the video at its orignal framerate.
# ~-~- frame by frame feature also allows automatic play on keyhold.
# .- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -.
#!/usr/bin/env python3
import cv2
yep = input("Enter the filename of your vod: ")
frorco = input("frame by frame or automatic : ")
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
def process_frame(img): 
    img = cv2.resize(img, (1920//2, 1080//2))
    cv2.imshow('image', img)
    if(frorco=="f"):
        cv2.waitKey(0)
    elif(frorco=="a"):
        cv2.waitKey(1)
    print(img.shape)
if __name__ == "__main__":
    cap = cv2.VideoCapture(yep)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
