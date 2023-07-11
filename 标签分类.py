#coding=utf-8
#python源码
import os
import shutil
import json

fileSourcePath = 'D:/Desktop/AgriculturalDisease_trainingset/images/'  #照片和json源文件路径
NewPath = 'label_data/'
filelist = os.listdir(fileSourcePath)
f = open('AgriculturalDisease_train_annotations.json', 'r')
content = f.read()
json_data = json.loads(content)
print(type(json_data))
print(json_data[0])
f.close()

j = 0
for filename in filelist: #遍历子目录文件夹
    s1=filename[:-3]+'jpg'
    everyFilePath = fileSourcePath  + str(filename)  #图片文件的路径名
    for i in json_data:
        s = i['image_id'][:-3] + 'jpg'
        if s1==s:
            dir=NewPath+str(i['disease_class'])
            if not os.path.exists(dir):
                os.makedirs(dir)
            shutil.move(everyFilePath, dir)
            j=j+1
print('共移动了{}个文件'.format(j))
print('分类完毕!')





