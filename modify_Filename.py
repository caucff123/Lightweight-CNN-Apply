#coding:utf-8
import os #导入模块
filename = 'D:/Desktop/白粉病/raw' #文件地址
list_path = os.listdir(filename)  #读取文件夹里面的名字
count=0;
for index in list_path:  #list_path返回的是一个列表   通过for循环遍历提取元素
    count=count+1;
    path = filename + '/' + index
    new_path = filename + '/'  + 'image_'+str(count)+'.jpg';
    os.rename(path, new_path) #重新命名

print('修改完成')