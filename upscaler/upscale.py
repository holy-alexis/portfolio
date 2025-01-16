import cv2


def upscale(name):
    img = cv2.imread(name, cv2.IMREAD_UNCHANGED)
    dim = (img.shape[1]*2, img.shape[0]*2)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(name, resized)
