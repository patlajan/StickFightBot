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
    hsv = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    b1 = np.array([240,240,240])
    b2 = np.array([255,255,255])
    img2 = cv2.inRange(hsv, b1, b2);
    
    cv2.imshow('Main', img2)
    return

def main():    
    cv2.startWindowThread()
    cv2.namedWindow("Main", cv2.WINDOW_AUTOSIZE)     
    hwnd = win32gui.FindWindow("Qt5QWindowIcon", "KOPLAYER 1.4.1055")
    rect = win32gui.GetClientRect(hwnd)
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    width = rect[2]
    height = rect[3]
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
        
    while(True):
        cDC.BitBlt((0,0),(width, height) , dcObj, (0,0), win32con.SRCCOPY)
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (height, width, 4)
        processImg(img)       
        cv2.waitKey(1) 
            
    cv2.destroyAllWindows()
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    
    return

main()