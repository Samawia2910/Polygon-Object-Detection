import json
import os
import cv2
import base64

import numpy as np


# with open('dataset/val/merge.json', 'r') as f:
#     f_train = json.load(f)
# # print(f_train)
# data_keys = list(f_train.keys())
# print(f_train)
# def pascal_voc_to_yolo(x1, y1, x2, y2, image_w, image_h):
#     return [((x2 + x1)/(2*image_w)), ((y2 + y1)/(2*image_h)), (x2 - x1)/image_w, (y2 - y1)/image_h]

def coco_to_yolo(x1, y1, x2, y2, image_w, image_h):
    return [((x2 + x1)/(2*image_w)), ((y2 + y1)/(2*image_h)), (x2 - x1)/image_w, (y2 - y1)/image_h]

for root,dir,files in os.walk('house_data_yolo/images', topdown=True):
    for file in files:
        print(file)
        if file.endswith('.bmp') or file.endswith('.jpg') or file.endswith('.png') or file.endswith('PNG') or file.endswith('JPG'):
            image_file = os.path.join(root, file)
            txt_file = file.split('.')[0]
            json_file = os.path.join('house_data_yolo/jsons/', txt_file+'.json')

            print(json_file)
            with open(json_file, 'r') as f:
                f_train = json.load(f)
            img = cv2.imread(image_file)
            h, w, c = img.shape
            # print(f_train['shapes'])
            yolo_ls =[]
            for shape in f_train['shapes']:
                # print(shape['points'])
                
                yolo_cor=coco_to_yolo(shape['points'][-1][0],shape['points'][-1][1],shape['points'][1][0],shape['points'][1][1],w,h)
                # print(yolo_ls)
                start_point=(int(shape['points'][-1][0]),int(shape['points'][-1][1]))
                end_point=(int(shape['points'][1][0]),int(shape['points'][1][1]))
                cv2.rectangle(img, start_point, end_point, [0,0,255], 1)
                # cv2.imshow('asd',img)
                # cv2.waitKey()
                arr= np.array(yolo_cor)
                yolo_ls.append(yolo_cor)
            with open(f'house_data_yolo/txt_yolo/{txt_file}.txt','w') as y:
                for  jp in yolo_ls:
                    arr=' '.join(str(v) for v in jp)
                    y.write('0'+' '+ arr +'\n')