from PIL import Image
import math
n=int(input("图片宽度: "))
m=int(input("图片高度: "))
def color_input(prompt):
    print(prompt)
    r=int(input("  红: "))
    g=int(input("  绿: "))
    b=int(input("  蓝: "))
    return (r,g,b)

a=color_input("初始颜色: ")
b=color_input("结束颜色: ")
im=Image.new('RGB',(n,m),(255,255,255))
for i in range(im.size[0]):
    for j in range(im.size[1]):
        ls1=[0,0,0]
        for k in range(3):
            weightb=(i+j)/(n+m)
            ls1[k]=int(a[k]*(1-weightb)+b[k]*weightb)
        im.putpixel((i,j),tuple(ls1))
        #print(ls1)

print("\n左上到右下: 1\n左下到右上: 2\n右上到左下: 3\n右下到左上: 4")
op=int(input("操作代码: "))
if op==1:
    im_out=im
if op==2:
    im_out=im.transpose(Image.FLIP_TOP_BOTTOM)
if op==3:
    im_out=im.transpose(Image.FLIP_LEFT_RIGHT)
if op==4:
    im_out=im.transpose(Image.ROTATE_180)
im_out.save(input("输出文件名: "))