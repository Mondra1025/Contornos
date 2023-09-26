import cv2
import numpy as np
valorgauss=1
valorkernel=50
original=cv2.imread('Monedas\Contorno\monedassoles.jpg')
gris=cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(gris,(valorgauss,valorgauss),0)
bordes=cv2.Canny(gauss,60,100)
kernel=np.ones((valorkernel,valorkernel),np.uint8)
cierre=cv2.morphologyEx(bordes,cv2.MORPH_CLOSE,kernel)
contornos, jerarquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("Monedas encontradas: {}".format(len(contornos)))
cv2.drawContours(original,contornos,-1,(0,0,255),2)
#v2.imshow("Grises",gris)
#v2.imshow("Desenfoque",gauss)
#v2.imshow("Canny",bordes)
#v2.imshow("Clausura",cierre)
cv2.imshow("Resultado",original)
cv2.waitKey(0)