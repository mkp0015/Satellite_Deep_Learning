from PIL import Image
from PIL import ImageColor
from create_colormap import make_cmap
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

fname = 'conus_goes_wv4km_0945.tif'
data = np.array(Image.open(fname))
    #if IR, set up IR parameters and calculate brightness temperature
if 'ir' in fname:
    cmap = 'sat_IR'
    ind = np.where(data > 176)
    ind2 = np.where(data <= 176)        
    pvar = np.zeros((data.shape[0],data.shape[1]),dtype=float)
    pvar[ind] = 418 - data[ind]
    pvar[ind2] = 330 - data[ind2]/2.

    #if WV, set up WV parameters and calculate brightness temperature
elif 'wv' in fname:
    cmap = 'sat_WV'
    ind = np.where(data > 176)
    ind2 = np.where(data <= 176)
    pvar = np.zeros((data.shape[0],data.shape[1]),dtype=float)
    pvar[ind] = 418 - data[ind]
    pvar[ind2] = 330 - data[ind2]/2.

    #else take the raw counts
else:
    cmap = 'gray'
    pvar = data

    #Create cmap for Satellite WV
if (cmap == 'sat_WV'):
    max_val = 273.
    min_val = 163.
    position = [0,(195.-min_val)/(max_val-min_val),
                (223.-min_val)/(max_val-min_val),
                (243.-min_val)/(max_val-min_val),
                (261.-min_val)/(max_val-min_val),
                (263.-min_val)/(max_val-min_val),1]
    ctable_path = os.path.join(r'C:\Users\mpullman\Desktop\class_scripts\class_scripts',cmap)
    new_cmap = make_cmap(ctable_path,position=position,bit=False)
    plt.register_cmap(cmap=new_cmap)
    
    #Create cmap for Satellite IR
elif (cmap == 'sat_IR'):
    max_val = 300.
    min_val = 170.
    position = [0,(200.-min_val)/(max_val-min_val),
                (208.-min_val)/(max_val-min_val),
                (218.-min_val)/(max_val-min_val),
                (228.-min_val)/(max_val-min_val),
                (245.-min_val)/(max_val-min_val),
                (253.-min_val)/(max_val-min_val),
                (258.-min_val)/(max_val-min_val),1]
    ctable_path = os.path.join(r'C:\Users\mpullman\Desktop\class_scripts\class_scripts',cmap)
    new_cmap = make_cmap(ctable_path,position=position,bit=False)
    plt.register_cmap(cmap=new_cmap)
    
    #use raw counts
else:
    min_val = 0
    max_val = 255
    new_cmap = cmap
        

print(np.nanmax(pvar),np.nanmin(pvar))

fig = plt.figure(figsize=(166.67,72.23),frameon=False)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(pvar,aspect='auto',cmap=new_cmap,vmin=min_val,vmax=max_val)
fig.savefig('testing2.png')
