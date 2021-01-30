import cv2
def cv2plt(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img