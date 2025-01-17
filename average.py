import numpy as np
import os
import cv2 as cv

def fill_boundary(img1, img2):  # img均为灰度图
    height1, width1 = img1.shape
    height2, width2 = img2.shape
    height = max(height1, height2)
    width = max(width1, width2)
    img1 = cv.copyMakeBorder(img1, (height - height1) // 2, (height - height1) // 2,
                              (width - width1) // 2, (width - width1) // 2, cv.BORDER_CONSTANT)
    img2 = cv.copyMakeBorder(img2, (height - height2) // 2, (height - height2) // 2,
                              (width - width2) // 2, (width - width2) // 2, cv.BORDER_CONSTANT)
    img1 = cv.resize(img1, (width, height), interpolation=cv.INTER_CUBIC)
    img2 = cv.resize(img2, (width, height), interpolation=cv.INTER_CUBIC)
    return img1, img2

class BBox(object):

    def __init__(self, bbox):
        self.left = bbox[0]
        self.top = bbox[1]
        self.right = bbox[2]
        self.bottom = bbox[3]

def average_pic(path,out_path):  # path为读取img_mean.jpg的文件夹名称，如bin_resize，bin_rotation，bin_rotation2
    if not os.path.exists(out_path):#建立输出文件夹
        os.makedirs(out_path)
    jujuba_name_list = os.listdir(path)
    img0 = cv.imread(os.path.join(path,jujuba_name_list[0]),cv.IMREAD_GRAYSCALE)
    img_black = np.zeros_like(img0)
    #img_mean_mean = cv.cvtColor(img_mean_mean, cv.COLOR_RGB2GRAY)
    n = len(jujuba_name_list)
    for jujuba_name in jujuba_name_list:
        img = cv.imread(os.path.join(path,jujuba_name), cv.IMREAD_GRAYSCALE)
        img_black, img = fill_boundary(img_black, img)
        img_black = img_black + (img / n)

    _, img_black = cv.threshold(img_black, 127, 255, cv.THRESH_BINARY)
    img_black = cv.medianBlur(img_black.astype(np.uint8), 5)
    cv.imwrite(out_path + 'mean.jpg', img_black)
    return img_black
"""
def option1(path):
    folder_list = os.listdir(path)  # 遍历子文件夹，生成子文件夹列表
    for folder in folder_list:  # 遍历文件夹
        new_path = os.path.join(path, folder)  # 子文件夹路径
        result = os.path.isdir(new_path)  # 判断输入文件夹下是否有文件夹
        
def option(input_path,output_path):
    if not os.path.exists(output_path):#建立输出文件夹
        os.makedirs(output_path)

    folder_list = os.listdir(input_path)  # 遍历子文件夹，生成子文件夹列表
    for folder in folder_list:  # 遍历文件夹
        new_path = os.path.join(input_path, folder)  # 子文件夹路径
        result = os.path.isdir(new_path)  # 判断输入文件夹下是否有文件夹
        if str(result) == 'True':
            1
"""