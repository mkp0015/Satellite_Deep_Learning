def make_cmap(colortable, position=None, bit=False):
    '''
    make_cmap takes a list of tuples which contain RGB values. The RGB
    values may either be in 8-bit [0 to 255] (in which bit must be set to
    True when called) or arithmetic [0 to 1] (default). make_cmap returns
    a cmap with equally spaced colors.
    Arrange your tuples so that the first color is the lowest value for the
    colorbar and the last is the highest.
    position contains values from 0 to 1 to dictate the location of each color.
    '''
    import matplotlib as mpl
    import numpy as np
    import os

    #Create full name
    file_path = colortable+'.txt'
    #Read file
    colors = np.loadtxt(file_path,skiprows=1)

    bit_rgb = np.linspace(0,1,256)
    if position == None:
        position = np.linspace(0,1,len(colors))
    else:
        if len(position) != len(colors):
            sys.exit("position length must be the same as colors")
        elif position[0] != 0 or position[-1] != 1:
            sys.exit("position must start with 0 and end with 1")
    if bit:
        for i in range(len(colors)):
            colors[i] = (bit_rgb[colors[i][0]],
                         bit_rgb[colors[i][1]],
                         bit_rgb[colors[i][2]])
    cdict = {'red':[], 'green':[], 'blue':[]}
    for pos, color in zip(position, colors):
        cdict['red'].append((pos, color[0], color[0]))
        cdict['green'].append((pos, color[1], color[1]))
        cdict['blue'].append((pos, color[2], color[2]))

    cmap = mpl.colors.LinearSegmentedColormap(os.path.basename(colortable),cdict,256)
    return cmap
    
def getCMAP(band):
    '''
    '''
    if band == 1:
        cmap = 'Greys_r'
    if band == 3:
        max_val = 273.
        min_val = 173.
        position = [0, (195. - min_val) / (max_val - min_val),
                   (223. - min_val) / (max_val - min_val),
                   (248. - min_val) / (max_val - min_val),
                   (261. - min_val) / (max_val - min_val),
                   (263. - min_val) / (max_val - min_val), 1]
        ncmap = create_colormap.make_cmap('sat_WV', position=position, bit=False)
        plt.register_cmap(cmap=ncmap)
        cmap = ncmap
    if band == 4:
        max_val = 300.
        min_val = 170.
        position = [0, (200. - min_val) / (max_val - min_val),
                   (208. - min_val) / (max_val - min_val),
                   (218. - min_val) / (max_val - min_val),
                   (228. - min_val) / (max_val - min_val),
                   (245. - min_val) / (max_val - min_val),
                   (253. - min_val) / (max_val - min_val),
                   (258. - min_val) / (max_val - min_val), 1]
        ncmap = create_colormap.make_cmap('sat_IR', position=position, bit=False)
        plt.register_cmap(cmap=ncmap)
        cmap = ncmap
    return cmap
