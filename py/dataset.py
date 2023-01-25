import os
import cv2
import glob
import csv
from csv import writer
from csv import reader
import numpy as np
from PIL import Image
import imutils

path1 = '/Users/insaf/OneDrive/Bureau/images/1/*'
path2 = '/Users/insaf/OneDrive/Bureau/images/2/*'
path3 = '/Users/insaf/OneDrive/Bureau/images/3/*'
path4 = '/Users/insaf/OneDrive/Bureau/images/4/*'
path5 = '/Users/insaf/OneDrive/Bureau/images/5/*'
path6 = '/Users/insaf/OneDrive/Bureau/images/6/*'
path7 = '/Users/insaf/OneDrive/Bureau/images/7/*'
path8 = '/Users/insaf/OneDrive/Bureau/images/8/*'
path9 = '/Users/insaf/OneDrive/Bureau/images/9/*'
path10 = '/Users/insaf/OneDrive/Bureau/images/10/*'
f = open('/Users/insaf/OneDrive/Bureau/data.csv', 'w')
writer = csv.writer(f)
reader = csv.reader(f)
row = "day","pixels","leaves", "leafsize_ave" ,"leafwidth_ave", "leafheight_ave", "leafarea_ave", "contourArea","width","height"
writer.writerow(row)
# 1er jour
for file in glob.glob(path1) :
    img= cv2.imread(file, 0)
    img2 = Image.open(file)
    img3= cv2.imread(file)
    ret, img_bin = cv2.threshold(img, 0 ,255,cv2.THRESH_BINARY)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    number_of_white_pix = np.sum(img_bin == 255)
    size = w, h = img2.size
    data = img2.load()
    color = []
    colors = []
    widths = []
    heights = []
    H = []
    W = []
    area = []
    Ar = []
    for x in range(w) :
      for y in range(h):
        color = data[x,y]
        colors.append(color)
    res = [*set(colors)]
    tot = len(res)-1
    leafsize = []
    for col in res:
      a = colors.count(col)
      leafsize.append(a) 
    leafsize.sort()
    m = len(leafsize)
    s = 0
    for i in range(m-1):
        s = s + leafsize[i]
    ave_leafsize = s/tot 
    numb_of_leaves = len(res)-1
    cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0] if len(cnt) == 2 else cnt[1]
    for c in cnt :
      xp,yp,wp,hp = cv2.boundingRect(c)
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      arp = cv2.contourArea(c)
      cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (50,100,250), 1)
    #blue
    mask = cv2.inRange(hsv, (110,100,100),(130,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(h)
      H.append(w)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))  
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])    
    H.clear()
    W.clear()  
    Ar.clear()

    #lightblue
    mask = cv2.inRange(hsv, (90,100,100),(110,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    #gray
    mask = cv2.inRange(hsv, (0,0,50),(360,255,160))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  
    
    #red
    mask = cv2.inRange(hsv, (0,100,100),(10,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2) 
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  

    #yellow
    mask = cv2.inRange(hsv, (20,100,100),(40,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(a) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear() 

    #green
    mask = cv2.inRange(hsv, (50,100,100),(70,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()
    
    #pink
    mask = cv2.inRange(hsv, (140,100,100),(150,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    ave_leafwidth = sum(widths)/tot
    ave_leafheight = sum(heights)/tot
    ave_leafarea = sum(area)/tot
    contour = arp
    width = wp
    height = hp
    row = '1' , number_of_white_pix , numb_of_leaves, ave_leafsize, ave_leafwidth, ave_leafheight, ave_leafarea, contour, width, height
    writer.writerow(row) 
# 2eme 
for file in glob.glob(path2) :
    img= cv2.imread(file, 0)
    img2 = Image.open(file)
    img3= cv2.imread(file)
    ret, img_bin = cv2.threshold(img, 0 ,255,cv2.THRESH_BINARY)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    number_of_white_pix = np.sum(img_bin == 255)
    size = w, h = img2.size
    data = img2.load()
    color = []
    colors = []
    widths = []
    heights = []
    H = []
    W = []
    area = []
    Ar = []
    for x in range(w) :
      for y in range(h):
        color = data[x,y]
        colors.append(color)
    res = [*set(colors)] 
    tot = len(res)-1
    leafsize = []
    for col in res:
      a = colors.count(col)
      leafsize.append(a) 
    leafsize.sort()
    m = len(leafsize)
    s = 0
    for i in range(m-1):
        s = s + leafsize[i]
    ave_leafsize = s/tot 
    numb_of_leaves = len(res)-1
    cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0] if len(cnt) == 2 else cnt[1]
    for c in cnt :
      xp,yp,wp,hp = cv2.boundingRect(c)
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      arp = cv2.contourArea(c)
      cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (50,100,250), 1)
    #blue
    mask = cv2.inRange(hsv, (110,100,100),(130,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(h)
      H.append(w)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))  
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])    
    H.clear()
    W.clear()  
    Ar.clear()

    #lightblue
    mask = cv2.inRange(hsv, (90,100,100),(110,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    #gray
    mask = cv2.inRange(hsv, (0,0,50),(360,255,160))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(a) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  
    
    #red
    mask = cv2.inRange(hsv, (0,100,100),(10,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2) 
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  

    #yellow
    mask = cv2.inRange(hsv, (20,100,100),(40,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear() 

    #green
    mask = cv2.inRange(hsv, (50,100,100),(70,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()
    
    #pink
    mask = cv2.inRange(hsv, (140,100,100),(150,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    ave_leafwidth = sum(widths)/tot
    ave_leafheight = sum(heights)/tot
    ave_leafarea = sum(area)/tot
    contour = arp
    width = wp
    height = hp
    row = '2' , number_of_white_pix, numb_of_leaves, ave_leafsize, ave_leafwidth, ave_leafheight, ave_leafarea, contour, width, height
    writer.writerow(row) 
# 3eme
for file in glob.glob(path3) :
    img= cv2.imread(file, 0)
    img2 = Image.open(file)
    img3= cv2.imread(file)
    ret, img_bin = cv2.threshold(img, 0 ,255,cv2.THRESH_BINARY)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    number_of_white_pix = np.sum(img_bin == 255)
    size = w, h = img2.size
    data = img2.load()
    color = []
    colors = []
    widths = []
    heights = []
    H = []
    W = []
    area = []
    Ar = []
    for x in range(w) :
      for y in range(h):
        color = data[x,y]
        colors.append(color)
    res = [*set(colors)] 
    tot = len(res)-1
    leafsize = []
    for col in res:
      a = colors.count(col)
      leafsize.append(a) 
    leafsize.sort()
    m = len(leafsize)
    s = 0
    for i in range(m-1):
        s = s + leafsize[i]
    ave_leafsize = s/tot 
    numb_of_leaves = len(res)-1
    #blue
    mask = cv2.inRange(hsv, (110,100,100),(130,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(h)
      H.append(w)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))  
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])    
    H.clear()
    W.clear()  
    Ar.clear()

    #lightblue
    mask = cv2.inRange(hsv, (90,100,100),(110,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    #gray
    mask = cv2.inRange(hsv, (0,0,50),(360,255,160))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(a) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  
    
    #red
    mask = cv2.inRange(hsv, (0,100,100),(10,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2) 
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  

    #yellow
    mask = cv2.inRange(hsv, (20,100,100),(40,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear() 

    #green
    mask = cv2.inRange(hsv, (50,100,100),(70,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()
    
    #pink
    mask = cv2.inRange(hsv, (140,100,100),(150,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    ave_leafwidth = sum(widths)/tot
    ave_leafheight = sum(heights)/tot
    ave_leafarea = sum(area)/tot
    contour = arp
    width = wp
    height = hp
    row = '3' , number_of_white_pix, numb_of_leaves, ave_leafsize, ave_leafwidth, ave_leafheight, ave_leafarea, contour, width, height
    writer.writerow(row)   
# 4eme
for file in glob.glob(path4) :
    img= cv2.imread(file, 0)
    img2 = Image.open(file)
    img3= cv2.imread(file)
    ret, img_bin = cv2.threshold(img, 0 ,255,cv2.THRESH_BINARY)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    number_of_white_pix = np.sum(img_bin == 255)
    size = w, h = img2.size
    data = img2.load()
    color = []
    colors = []
    widths = []
    heights = []
    H = []
    W = []
    area = []
    Ar = []
    for x in range(w) :
      for y in range(h):
        color = data[x,y]
        colors.append(color)
    res = [*set(colors)] 
    tot = len(res)-1
    leafsize = []
    for col in res:
      a = colors.count(col)
      leafsize.append(a) 
    leafsize.sort()
    m = len(leafsize)
    s = 0
    for i in range(m-1):
        s = s + leafsize[i]
    ave_leafsize = s/tot 
    numb_of_leaves = len(res)-1
    cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0] if len(cnt) == 2 else cnt[1]
    for c in cnt :
      xp,yp,wp,hp = cv2.boundingRect(c)
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      arp = cv2.contourArea(c)
      cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (50,100,250), 1)
    #blue
    mask = cv2.inRange(hsv, (110,100,100),(130,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(h)
      H.append(w)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))  
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])    
    H.clear()
    W.clear()  
    Ar.clear()

    #lightblue
    mask = cv2.inRange(hsv, (90,100,100),(110,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    #gray
    mask = cv2.inRange(hsv, (0,0,50),(360,255,160))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(a) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  
    
    #red
    mask = cv2.inRange(hsv, (0,100,100),(10,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2) 
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  

    #yellow
    mask = cv2.inRange(hsv, (20,100,100),(40,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear() 

    #green
    mask = cv2.inRange(hsv, (50,100,100),(70,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()
    
    #pink
    mask = cv2.inRange(hsv, (140,100,100),(150,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()


    ave_leafwidth = sum(widths)/tot
    ave_leafheight = sum(heights)/tot
    ave_leafarea = sum(area)/tot
    contour = arp
    width = wp
    height = hp
    row = '4' , number_of_white_pix, numb_of_leaves, ave_leafsize, ave_leafwidth, ave_leafheight, ave_leafarea, contour, width, height
    writer.writerow(row)
# 5eme
for file in glob.glob(path5) :
    img= cv2.imread(file, 0)
    img2 = Image.open(file)
    img3= cv2.imread(file)
    ret, img_bin = cv2.threshold(img, 0 ,255,cv2.THRESH_BINARY)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    number_of_white_pix = np.sum(img_bin == 255)
    size = w, h = img2.size
    data = img2.load()
    color = []
    colors = []
    widths = []
    heights = []
    H = []
    W = []
    area = []
    Ar = []
    for x in range(w) :
      for y in range(h):
        color = data[x,y]
        colors.append(color)
    res = [*set(colors)] 
    tot = len(res)-1
    leafsize = []
    for col in res:
      a = colors.count(col)
      leafsize.append(a) 
    leafsize.sort()
    m = len(leafsize)
    s = 0
    for i in range(m-1):
        s = s + leafsize[i]
    ave_leafsize = s/tot 
    numb_of_leaves = len(res)-1
    cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0] if len(cnt) == 2 else cnt[1]
    for c in cnt :
      xp,yp,wp,hp = cv2.boundingRect(c)
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      arp = cv2.contourArea(c)
      cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (50,100,250), 1)
    #blue
    mask = cv2.inRange(hsv, (110,100,100),(130,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(h)
      H.append(w)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))  
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])    
    H.clear()
    W.clear()  
    Ar.clear()

    #lightblue
    mask = cv2.inRange(hsv, (90,100,100),(110,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    #gray
    mask = cv2.inRange(hsv, (0,0,50),(360,255,160))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(a) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  
    
    #red
    mask = cv2.inRange(hsv, (0,100,100),(10,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2) 
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  

    #yellow
    mask = cv2.inRange(hsv, (20,100,100),(40,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear() 

    #green
    mask = cv2.inRange(hsv, (50,100,100),(70,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()
    
    #pink
    mask = cv2.inRange(hsv, (140,100,100),(150,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()


    ave_leafwidth = sum(widths)/tot
    ave_leafheight = sum(heights)/tot
    ave_leafarea = sum(area)/tot
    contour = arp
    width = wp
    height = hp
    row = '5' , number_of_white_pix, numb_of_leaves, ave_leafsize, ave_leafwidth, ave_leafheight, ave_leafarea, contour, width, height
    writer.writerow(row)
# 6eme
for file in glob.glob(path6) :
    img= cv2.imread(file, 0)
    img2 = Image.open(file)
    img3= cv2.imread(file)
    ret, img_bin = cv2.threshold(img, 0 ,255,cv2.THRESH_BINARY)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    number_of_white_pix = np.sum(img_bin == 255)
    size = w, h = img2.size
    data = img2.load()
    color = []
    colors = []
    widths = []
    heights = []
    H = []
    W = []
    area = []
    Ar = []
    for x in range(w) :
      for y in range(h):
        color = data[x,y]
        colors.append(color)
    res = [*set(colors)] 
    tot = len(res)-1
    leafsize = []
    for col in res:
      a = colors.count(col)
      leafsize.append(a) 
    leafsize.sort()
    m = len(leafsize)
    s = 0
    for i in range(m-1):
        s = s + leafsize[i]
    ave_leafsize = s/tot 
    numb_of_leaves = len(res)-1
    cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0] if len(cnt) == 2 else cnt[1]
    for c in cnt :
      xp,yp,wp,hp = cv2.boundingRect(c)
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      arp = cv2.contourArea(c)
      cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (50,100,250), 1)
    #blue
    mask = cv2.inRange(hsv, (110,100,100),(130,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(h)
      H.append(w)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))  
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])    
    H.clear()
    W.clear()  
    Ar.clear()

    #lightblue
    mask = cv2.inRange(hsv, (90,100,100),(110,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    #gray
    mask = cv2.inRange(hsv, (0,0,50),(360,255,160))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(a) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  
    
    #red
    mask = cv2.inRange(hsv, (0,100,100),(10,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2) 
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  

    #yellow
    mask = cv2.inRange(hsv, (20,100,100),(40,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear() 

    #green
    mask = cv2.inRange(hsv, (50,100,100),(70,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()
    
    #pink
    mask = cv2.inRange(hsv, (140,100,100),(150,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()


    ave_leafwidth = sum(widths)/tot
    ave_leafheight = sum(heights)/tot
    ave_leafarea = sum(area)/tot
    contour = arp
    width = wp
    height = hp
    row = '6' , number_of_white_pix, numb_of_leaves, ave_leafsize, ave_leafwidth, ave_leafheight, ave_leafarea, contour, width, height
    writer.writerow(row)
# 7eme
for file in glob.glob(path7) :
    img= cv2.imread(file, 0)
    img2 = Image.open(file)
    img3= cv2.imread(file)
    ret, img_bin = cv2.threshold(img, 0 ,255,cv2.THRESH_BINARY)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    number_of_white_pix = np.sum(img_bin == 255)
    size = w, h = img2.size
    data = img2.load()
    color = []
    colors = []
    widths = []
    heights = []
    H = []
    W = []
    area = []
    Ar = []
    for x in range(w) :
      for y in range(h):
        color = data[x,y]
        colors.append(color)
    res = [*set(colors)] 
    tot = len(res)-1
    leafsize = []
    for col in res:
      a = colors.count(col)
      leafsize.append(a) 
    leafsize.sort()
    m = len(leafsize)
    s = 0
    for i in range(m-1):
        s = s + leafsize[i]
    ave_leafsize = s/tot 
    numb_of_leaves = len(res)-1
    cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0] if len(cnt) == 2 else cnt[1]
    for c in cnt :
      xp,yp,wp,hp = cv2.boundingRect(c)
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      arp = cv2.contourArea(c)
      cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (50,100,250), 1)
    #blue
    mask = cv2.inRange(hsv, (110,100,100),(130,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(h)
      H.append(w)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))  
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])    
    H.clear()
    W.clear()  
    Ar.clear()

    #lightblue
    mask = cv2.inRange(hsv, (90,100,100),(110,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    #gray
    mask = cv2.inRange(hsv, (0,0,50),(360,255,160))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(a) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  
    
    #red
    mask = cv2.inRange(hsv, (0,100,100),(10,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2) 
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  

    #yellow
    mask = cv2.inRange(hsv, (20,100,100),(40,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear() 

    #green
    mask = cv2.inRange(hsv, (50,100,100),(70,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()
    
    #pink
    mask = cv2.inRange(hsv, (140,100,100),(150,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    ave_leafwidth = sum(widths)/tot
    ave_leafheight = sum(heights)/tot
    ave_leafarea = sum(area)/tot
    contour = arp
    width = wp
    height = hp
    row = '7' , number_of_white_pix, numb_of_leaves, ave_leafsize, ave_leafwidth, ave_leafheight, ave_leafarea, contour, width, height
    writer.writerow(row)                    
# 8eme
for file in glob.glob(path8) :
    img= cv2.imread(file, 0)
    img2 = Image.open(file)
    img3= cv2.imread(file)
    ret, img_bin = cv2.threshold(img, 0 ,255,cv2.THRESH_BINARY)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    number_of_white_pix = np.sum(img_bin == 255)
    size = w, h = img2.size
    data = img2.load()
    color = []
    colors = []
    widths = []
    heights = []
    H = []
    W = []
    area = []
    Ar = []
    for x in range(w) :
      for y in range(h):
        color = data[x,y]
        colors.append(color)
    res = [*set(colors)] 
    tot = len(res)-1
    leafsize = []
    for col in res:
      a = colors.count(col)
      leafsize.append(a) 
    leafsize.sort()
    m = len(leafsize)
    s = 0
    for i in range(m-1):
        s = s + leafsize[i]
    ave_leafsize = s/tot 
    numb_of_leaves = len(res)-1
    cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0] if len(cnt) == 2 else cnt[1]
    for c in cnt :
      xp,yp,wp,hp = cv2.boundingRect(c)
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      arp = cv2.contourArea(c)
      cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (50,100,250), 1)
    #blue
    mask = cv2.inRange(hsv, (110,100,100),(130,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(h)
      H.append(w)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))  
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])    
    H.clear()
    W.clear()  
    Ar.clear()

    #lightblue
    mask = cv2.inRange(hsv, (90,100,100),(110,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    #gray
    mask = cv2.inRange(hsv, (0,0,50),(360,255,160))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(a) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  
    
    #red
    mask = cv2.inRange(hsv, (0,100,100),(10,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2) 
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  

    #yellow
    mask = cv2.inRange(hsv, (20,100,100),(40,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear() 

    #green
    mask = cv2.inRange(hsv, (50,100,100),(70,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()
    
    #pink
    mask = cv2.inRange(hsv, (140,100,100),(150,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()


    ave_leafwidth = sum(widths)/tot
    ave_leafheight = sum(heights)/tot
    ave_leafarea = sum(area)/tot
    contour = arp
    width = wp
    height = hp
    row = '8' , number_of_white_pix, numb_of_leaves, ave_leafsize, ave_leafwidth, ave_leafheight, ave_leafarea, contour, width, height
    writer.writerow(row)           
# 9eme
for file in glob.glob(path9) :
    img= cv2.imread(file, 0)
    img2 = Image.open(file)
    img3= cv2.imread(file)
    ret, img_bin = cv2.threshold(img, 0 ,255,cv2.THRESH_BINARY)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    number_of_white_pix = np.sum(img_bin == 255)
    size = w, h = img2.size
    data = img2.load()
    color = []
    colors = []
    widths = []
    heights = []
    H = []
    W = []
    area = []
    Ar = []
    for x in range(w) :
      for y in range(h):
        color = data[x,y]
        colors.append(color)
    res = [*set(colors)] 
    tot = len(res)-1
    leafsize = []
    for col in res:
      a = colors.count(col)
      leafsize.append(a) 
    leafsize.sort()
    m = len(leafsize)
    s = 0
    for i in range(m-1):
        s = s + leafsize[i]
    ave_leafsize = s/tot 
    numb_of_leaves = len(res)-1
    cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0] if len(cnt) == 2 else cnt[1]
    for c in cnt :
      xp,yp,wp,hp = cv2.boundingRect(c)
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      arp = cv2.contourArea(c)
      cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (50,100,250), 1)
    #blue
    mask = cv2.inRange(hsv, (110,100,100),(130,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(h)
      H.append(w)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))  
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])    
    H.clear()
    W.clear()  
    Ar.clear()

    #lightblue
    mask = cv2.inRange(hsv, (90,100,100),(110,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    #gray
    mask = cv2.inRange(hsv, (0,0,50),(360,255,160))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  
    
    #red
    mask = cv2.inRange(hsv, (0,100,100),(10,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2) 
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  

    #yellow
    mask = cv2.inRange(hsv, (20,100,100),(40,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear() 

    #green
    mask = cv2.inRange(hsv, (50,100,100),(70,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()
    
    #pink
    mask = cv2.inRange(hsv, (140,100,100),(150,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    ave_leafwidth = sum(widths)/tot
    ave_leafheight = sum(heights)/tot
    ave_leafarea = sum(area)/tot
    contour = arp
    width = wp
    height = hp
    row = '9' , number_of_white_pix, numb_of_leaves, ave_leafsize, ave_leafwidth, ave_leafheight, ave_leafarea, contour, width, height
    writer.writerow(row)
# 10eme
for file in glob.glob(path10) :
    img= cv2.imread(file, 0)
    img2 = Image.open(file)
    img3= cv2.imread(file)
    ret, img_bin = cv2.threshold(img, 0 ,255,cv2.THRESH_BINARY)
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    number_of_white_pix = np.sum(img_bin == 255)
    size = w, h = img2.size
    data = img2.load()
    color = []
    colors = []
    widths = []
    heights = []
    H = []
    W = []
    area = []
    Ar = []
    for x in range(w) :
      for y in range(h):
        color = data[x,y]
        colors.append(color)
    res = [*set(colors)] 
    tot = len(res)-1
    leafsize = []
    for col in res:
      a = colors.count(col)
      leafsize.append(a) 
    leafsize.sort()
    m = len(leafsize)
    s = 0
    for i in range(m-1):
        s = s + leafsize[i]
    ave_leafsize = s/tot 
    numb_of_leaves = len(res)-1
    cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0] if len(cnt) == 2 else cnt[1]
    for c in cnt :
      xp,yp,wp,hp = cv2.boundingRect(c)
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      arp = cv2.contourArea(c)
      cv2.rectangle(img, (xp, yp), (xp + wp, yp + hp), (50,100,250), 1)
    #blue
    mask = cv2.inRange(hsv, (110,100,100),(130,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(h)
      H.append(w)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))  
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])    
    H.clear()
    W.clear()  
    Ar.clear()

    #lightblue
    mask = cv2.inRange(hsv, (90,100,100),(110,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()

    #gray
    mask = cv2.inRange(hsv, (0,0,50),(360,255,160))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  
    
    #red
    mask = cv2.inRange(hsv, (0,100,100),(10,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2) 
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()  

    #yellow
    mask = cv2.inRange(hsv, (20,100,100),(40,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear() 

    #green
    mask = cv2.inRange(hsv, (50,100,100),(70,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)    
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()
    
    #pink
    mask = cv2.inRange(hsv, (140,100,100),(150,255,255))
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts :
      Ar.append(cv2.contourArea(c))
      cv2.drawContours(img, [c], -1, (255,255,255), 3)
      x,y,w,h = cv2.boundingRect(c)
      W.append(w)
      H.append(h)
      cv2.rectangle(img, (x, y), (x + w, y + h), (50,100,250), 2)  
      if len(W) >= 2 and len(H) >= 2 :
        heights.append(max(H))
        widths.append(max(W))
      else :
        heights.append(H[0])  
        widths.append(W[0])
      if len(Ar) >= 2 :
        area.append(max(Ar))
      else :
        area.append(Ar[0])   
    H.clear()
    W.clear()    
    Ar.clear()


    ave_leafwidth = sum(widths)/tot
    ave_leafheight = sum(heights)/tot
    ave_leafarea = sum(area)/tot
    contour = arp
    width = wp
    height = hp
    row = '10' , number_of_white_pix, numb_of_leaves, ave_leafsize, ave_leafwidth, ave_leafheight, ave_leafarea, contour, width, height
    writer.writerow(row)

f.close()