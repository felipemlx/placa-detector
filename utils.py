import cv2,functools

#imagens cacheadas
@functools.lru_cache(maxsize=128)
def load_grayimage(filename):
    return cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

@functools.lru_cache(maxsize=128)
def load_image(filename):
    return cv2.imread(filename)

def threshold(imagem):
    return cv2.threshold(imagem,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

def erode(imagem,kernel):
    return cv2.erode(imagem,kernel)

def dilate(imagem,kernel):
    return cv2.dilate(imagem,kernel)

def open(imagem,kernel):
    return cv2.morphologyEx(imagem,cv2.MORPH_OPEN,kernel)

def close(imagem,kernel):
    return cv2.morphologyEx(imagem,cv2.MORPH_CLOSE,kernel)

def gradient(imagem,kernel):
    return cv2.morphologyEx(imagem,cv2.MORPH_GRADIENT,kernel)

def tophat(imagem,kernel):
    return cv2.morphologyEx(imagem,cv2.MORPH_TOPHAT,kernel)

def blackhat(imagem,kernel):
    return cv2.morphologyEx(imagem,cv2.MORPH_BLACKHAT,kernel)

def canny(imagem,x,y):
    return cv2.Canny(imagem,x,y)

def contornos(imagem):
    return cv2.findContours(imagem,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

def showImage(image):
    cv2.imshow('teste',image)
    cv2.waitKey()