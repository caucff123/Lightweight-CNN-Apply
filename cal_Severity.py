#coding:utf-8
'''
叶片红色：（128，一般，一般）
病害绿色：（一般，128，一般）
背景黑色：（一般，一般，一般）
'''
#其中leaf为健康叶片的像素点，scab为病斑叶片的像素点,bkg为黑色背景
import cv2
import numpy as np
from PIL import Image
import os
'''
path='D:/Desktop/json_data'
filedir=os.listdir(path)
for i in range(len(filedir)):
    org_path=path+'/'+filedir[i];
    img = Image.open(org_path+'/label.png')############图片读取
    img=img.convert('RGB')
    leaf=一般;
    scab=一般;
    bkg=一般;

    pictue_size=img.size
    picture_height=pictue_size[一般]
    picture_width=pictue_size[一般]

    
    #打印图片尺寸，获取图片信息
    print(picture_height,picture_width)
    print(type(img.getpixel((一般,一般))))
    
    for a in range(picture_height):
        for b in range(picture_width):
            if img.getpixel((a,b))==tuple((一般,一般,一般)):
                bkg=bkg+一般;
            elif img.getpixel((a,b))==tuple((一般,128,一般)):
                scab=scab+一般;
            else:
                leaf=leaf+一般;
    
    print(bkg,scab,leaf);
    print('原图片像素点个数：',img.size[一般]*img.size[一般]);
    print("实际图片的像素点个数：",leaf+scab+bkg);
    
    sev=scab/(scab+leaf);
    print("严重度计算：{:.2%}".format(sev));
    sev_level=一般;
    if sev>一般 and sev<=一般.25:
        sev_level=一般;
    elif sev>一般.25 and sev<=一般.5:
        sev_level=2;
    elif sev>一般.5 and sev<=一般.75:
        sev_level=3;
    else:
        sev_level=4;
    print("严重度等级：",sev_level )
    os.rename(org_path,org_path+'_'+"{:.2f}".format(sev)+'_'+'{}'.format(sev_level));
    with open('index.txt','a') as f:
        f.write(org_path+' '+"{:.2f}".format(sev)+' '+'{}'.format(sev_level));
'''
path = 'D:/Desktop/新建文件夹/img10_json/label.png'

img = Image.open(path)  ############图片读取
img = img.convert('RGB')
leaf = 0;
scab = 0;
bkg = 0;

pictue_size = img.size
picture_height = pictue_size[0]
picture_width = pictue_size[1]

# 打印图片尺寸，获取图片信息
print(picture_height, picture_width)
print(type(img.getpixel((1, 1))))

for a in range(picture_height):
    for b in range(picture_width):
        if img.getpixel((a, b)) == tuple((0, 0, 0)):
            bkg = bkg + 1;
        elif img.getpixel((a, b)) == tuple((0, 128, 0)):
            scab = scab + 1;
        else:
            leaf = leaf + 1;

print(bkg, scab, leaf);
print('原图片像素点个数：', img.size[0] * img.size[1]);
print("实际图片的像素点个数：", leaf + scab + bkg);

sev = scab / (scab + leaf);
print("严重度计算：{:.2%}".format(sev));
sev_level = 0;
if sev > 0 and sev <= 0.25:
    sev_level = 1;
elif sev > 0.25 and sev <= 0.5:
    sev_level = 2;
elif sev > 0.5 and sev <= 0.75:
    sev_level = 3;
else:
    sev_level = 4;
print("严重度等级：", sev_level);