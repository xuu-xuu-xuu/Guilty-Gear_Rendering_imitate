"""Deterministic checks on real Unity PNGs; no image synthesis or retouching."""
from PIL import Image, ImageChops, ImageStat

def rgb(path):
    with Image.open(path) as im:
        return im.convert('RGB')

def change_mask(a,b):
    channels=ImageChops.difference(a,b).split()
    return ImageChops.lighter(ImageChops.lighter(channels[0],channels[1]),channels[2]).point(lambda v:255 if v else 0)

def compare(a,b):
    assert a.size==b.size
    d=ImageChops.difference(a,b)
    mask=change_mask(a,b)
    return {'dimensions':list(a.size),'changedPixels':mask.histogram()[255],
            'changedBBoxXYXY':list(mask.getbbox()) if mask.getbbox() else None,
            'maxChannelDifference':max(x[1] for x in d.getextrema()),
            'meanAbsoluteRGB':sum(ImageStat.Stat(d).mean)/3}

def eye_coverage(debug_image):
    # Debug33 uses separate R/G/B regions; gray backdrop is not an eye mask.
    mask=Image.new('L',debug_image.size)
    mask.putdata([255 if max(p)>min(p) else 0 for p in debug_image.getdata()])
    return mask

def outside_count(a,b,mask):
    return ImageChops.subtract(change_mask(a,b),mask).histogram()[255]
