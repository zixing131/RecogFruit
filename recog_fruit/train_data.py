#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   train_data.py    
@Contact :   971680807@qq.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/24 15:49   唐永金      1.0         None
'''
import os
import skimage
from skimage import data,transform

data_path='C:/Users/Administrator/Desktop/fruit_test/'
def loadsmall_data(dir_path,m=20):#20种水果
    images_m=[]
    labels_m=[]
    lab=os.listdir(dir_path)
    n=0
    for l in lab:
        if (n>=m):
           break
        print('读取'+str(n)+'-'+l)
        img=os.listdir(dir_path+l)
        for i in img:
           img_path=dir_path+l+'/'+i
           labels_m.append(int(n))
           images_m.append(skimage.data.imread(img_path))
        n+=1
    return images_m,labels_m
##批量裁剪
def cut_image(images,w,h):
    return [skimage.transform.resize(I,(w,h)) for I in images]

if __name__ == '__main__':
    images_m, labels_m=loadsmall_data(data_path,2)
