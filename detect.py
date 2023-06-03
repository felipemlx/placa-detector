import pytesseract, utils, cv2, re as regex
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
tesseract_config_texto = '--tessdata-dir tessdata --psm 6'

class Detector():
    def __init__(self):
        self.count = 0
        #Extrair texto da placa
        print(self.extrairTextoPlaca('img/placa1.png',doErode = True))
        print(self.extrairTextoPlaca('img/placa2.jpg'))
        print(self.extrairTextoPlaca('img/placa3.jpg'))
        print(self.extrairTextoPlaca('img/placa4.jpg',doErode = True))
        print(self.extrairTextoPlaca('img/placa5.webp',doErode = True))
            
    def extrairTextoPlaca(self,filename,doErode = False):
        #Load na imagem cacheada em escala de cinza
        imagem_gray = utils.load_grayimage(filename)
        #Definir bordas e contornos da placa
        bordas = utils.canny(imagem_gray,100,200)
        contornos,_ = utils.contornos(bordas)
        #Como a imagem pode ter muitos contornos, vou extrair os 10 contornos de maior área encontrados
        contornos = sorted(contornos,key = cv2.contourArea, reverse=True)[:10]
        for contorno in contornos:
            eps = 0.02 * cv2.arcLength(contorno,True)
            aprox = cv2.approxPolyDP(contorno,eps,True)
            if cv2.isContourConvex(aprox) and len(aprox) == 4:
                loc = aprox
                break
            loc = None
        if loc is None:
            return 'Não encontrou placa.'
        #Cortar a imagem no retângulo localizado da placa
        x,y, width, height = cv2.boundingRect(loc)
        placa_cortada = imagem_gray[y:y+height, x:x+width]
        #Fazer limiarização (threshold) e erosão (erode), se necessário
        val,threshold = utils.threshold(placa_cortada)
        #utils.showImage(threshold)
        if doErode:
            threshold = utils.erode(threshold,cv2.getStructuringElement(cv2.MORPH_RECT,(4,4)))
        #Aplicar tesseract
        texto = pytesseract.image_to_string(threshold,lang='por',config = tesseract_config_texto)
        if texto is not None:
            #print('Placa sem filtro: ',texto)
            return self.filtrarTexto(texto)
        return None

    def filtrarTexto(self,texto):
        self.count += 1
        #Expressão regular das placas: 3 letras -> 1 número -> 1 letra -> 2 números
        texto_extraido = regex.search('\w{3}\d{1}\w{1}\d{2}',texto)
        if texto_extraido is not None:
            texto_extraido = texto_extraido.group(0)
            return f'Placa{self.count}: {texto_extraido}'

detector = Detector()