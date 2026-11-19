import sys, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
src, out, thr = sys.argv[1], sys.argv[2], float(sys.argv[3])
im = np.asarray(Image.open(src).convert('RGB')).astype(np.int16)
r,g,b = im[...,0],im[...,1],im[...,2]
warm = (r-b)
bg = np.array([246,241,235])
dist = np.abs(im-bg).sum(-1)
fg = (warm < thr) | (dist > 120) & (warm < thr+6)
fg = ndimage.binary_opening(fg, iterations=int(sys.argv[4]) if len(sys.argv)>4 else 2)
lab,n = ndimage.label(fg); sizes = ndimage.sum(fg,lab,range(1,n+1))
keep = np.isin(lab, [i+1 for i,s in enumerate(sizes) if s > 0.02*fg.sum()])
keep = ndimage.binary_fill_holes(ndimage.binary_closing(keep, iterations=6))
a = Image.fromarray((keep*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.5))
o = Image.open(src).convert('RGBA'); o.putalpha(a); o = o.crop(o.getbbox()); o.save(out)
print(out, o.size)
