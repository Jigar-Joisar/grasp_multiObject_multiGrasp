import numpy as np    
import imageio as i
import os
import glob

txt_names = glob.glob(os.path.join('./output12/'+'*.txt')) 
#print(txt_names)
lines = []
for t in txt_names:
  f = open(t)
  lines = [Line.rstrip() for Line in f]
  #print(lines)

co = lines[0].split()
#print(co)
x1 = int(co[0])
y1 = int(co[1])
x2 = int(co[2])
y2 = int(co[3])

mask = np.zeros((480,640))
mask[y1:y2,x1:x2]=1
i.imwrite('mask.jpg', mask)
