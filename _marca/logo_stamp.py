import sys
from PIL import Image
def stamp(path, variant, height=88, margin=(110,60)):
    im=Image.open(path).convert('RGB'); W,H=im.size
    lg=Image.open(f''+__import__("os").path.dirname(__file__)+'/logo-{variant}.png')
    w=int(lg.width*height/lg.height); lg=lg.resize((w,height),Image.LANCZOS)
    im.paste(lg,(W-margin[0]-w,H-margin[1]-height),lg)
    im.save(path,quality=84,optimize=True,progressive=True)
if __name__=='__main__': stamp(sys.argv[1],sys.argv[2])
