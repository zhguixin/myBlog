# -*- coding: UTF-8 -*-
'''
Created on 2018年1月14日

@author: zhguixin

pip install piexif
修改 IOS设备EXIF的 Orientation 信息
'''
import os
from PIL import Image, ExifTags
import piexif
import json

INFO = '.info'
baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mediaPath = os.path.join(baseDir, 'static', 'media')
galleryPath = os.path.join(baseDir, 'static', 'gallery')
img_str=('.jpg','.pgm','.bmp','.jpeg', '.JPG', '.JPEG', '.BMP')

def scan_imgs():
    for root, sub_dirs, files in os.walk(mediaPath):
        # print root, sub_dirs, files
        for file in files:
            # 过滤掉非图片格式的文件，以及以【thumbnail】开头的文件
            if file.startswith('thumbnail') or (not file.endswith(img_str)):
                continue;
            print file
            # generator_descriptio_file(file.split('.')[0])
            compress(file)

# 压缩图片，生成对应的缩略图
def compress(img_name):
    img = os.path.join(mediaPath, img_name)
    image = Image.open(img)  # 通过img 获得图像  
    width = image.width 
    height = image.height
    rate = 1.0 # 压缩率

    # 根据图像大小设置压缩率
    if width >= 2000 or height >= 2000:
        rate = 0.3
    elif width >= 1000 or height >= 1000:
        rate = 0.5
    elif width >= 500 or height >= 500:
        rate = 0.9

    print width, height, rate
#     print json.dumps(image._getexif(), encoding="UTF-8", ensure_ascii=False)
    width = int(width * rate)   # 新的宽
    height = int(height * rate) # 新的高

    print width, height
    image.thumbnail((width, height), Image.ANTIALIAS) # 生成缩略图
    image.save(os.path.join(mediaPath, 'thumbnail_' + img_name), 'JPEG')    # 保存到原路径

# 为每一个图片文件生成相应的描述文件
def generator_descriptio_file(name):
    path = os.path.join(mediaPath, name)
    description_file = open(path + INFO, 'wb')
    description_file.write('')
    description_file.close()

# 生成json配置文件
def generator_json():
    gallery = []
    group = {}
    for root, sub_dirs, files in os.walk(mediaPath):
    # print root, sub_dirs, files
        for file in files:
            # 过滤掉非图片格式的文件，以及以【thumbnail】开头的文件
            if file.endswith(img_str) and file.startswith('thumbnail'):
                group['thumbnail_path'] = '/static/media/' + file;
            if file.endswith(img_str) and not file.startswith('thumbnail'):
                group['img_path'] = '/static/media/' + file;
            if file.startswith(file.split('.')[0]) and file.endswith(INFO):
                path = os.path.join(mediaPath, file.split('.')[0]);
                description_file = open(path + INFO, 'rb');
                print description_file.read();
                group['description'] = description_file.read();
                description_file.close();
            print group
            gallery.append(group)

    # 保存到json文件
    json_file = open(mediaPath + '/gallery.json', 'wb')
    json_file.write(json.dumps(gallery))
    json_file.close()

def get_exif():
    for root, sub_dirs, files in os.walk(galleryPath):
        # print root, sub_dirs, files
        img = os.path.join(galleryPath, files[3])
        image = Image.open(img)
        for tag, value in image._getexif().items():
            print ExifTags.TAGS.get(tag), value
        for file in files:
            print file

def change_exif():
    img = os.path.join(galleryPath, 'IMG_0055.JPG')
    new_file = os.path.join(galleryPath, 'IMG_0055_1.JPG')
    image = Image.open(new_file)
    for tag, value in image._getexif().items():
        print tag, ExifTags.TAGS.get(tag), value
#     exif_dict = piexif.load(image.info["exif"])
#     exif_dict["0th"][piexif.ImageIFD.Orientation] = 1
#     exif_bytes = piexif.dump(exif_dict)
#     image.save(new_file, "jpeg", exif=exif_bytes)

if __name__ == '__main__':
#     scan_imgs()
#     generator_json()
#     get_exif()
    change_exif()
