from PIL import Image
from PIL import ImageDraw
 
imgPath="C:\\Users\\Administrator\\Desktop\\a.jpg"
x=0
y=0
w=h=604
r=30
im = Image.open(imgPath)
drawObject = ImageDraw.Draw(im)

'''Rounds'''    
drawObject.ellipse((x,y,x+r,y+r),fill=0)    
drawObject.ellipse((x+w-r,y,x+w,y+r),fill=0)    
drawObject.ellipse((x,y+h-r,x+r,y+h),fill=0)    
drawObject.ellipse((x+w-r,y+h-r,x+w,y+h),fill=0)

'''rec.s'''    
drawObject.rectangle((x+r/2,y, x+w-(r/2), y+h),fill=0)    
drawObject.rectangle((x,y+r/2, x+w, y+h-(r/2)),fill=0)
im.show()

 