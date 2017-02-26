import win32gui
import win32ui
import win32api
import win32con
import ImageGrab
import time
import cv2 as cv2
from array import array
import numpy as np

def processImg(img):
    cv2.imshow('Main', img)
    return

def main():    
    cv2.startWindowThread()
    cv2.namedWindow("Main", cv2.WINDOW_AUTOSIZE)     
    hwnd = win32gui.FindWindow(None, "Play Stick Fight game online - Y8.COM")
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, 1920, 1080)
    cDC.SelectObject(dataBitMap)
        
    while(True):
        cDC.BitBlt((0,0),(1920, 1080) , dcObj, (0,0), win32con.SRCCOPY)
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (1080,1920,4)
        processImg(img)       
        cv2.waitKey(1) 
            
    cv2.destroyAllWindows()
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    
    return

main()