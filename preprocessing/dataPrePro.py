# coding=utf-8

import json
import csv
import numpy as np
import pandas as pd
rele_path = 'data/imgs/'
class_list = {}

def json_to_csv(json_file, flag):

    json_list = json.load(json_file)
    img_path = []
    xmin_list = []
    xmax_list = []
    ymin_list = []
    ymax_list = []
    cate_list = []
    # max_size = 0
    # min_size = 10000000
    num = 0
    for dict in json_list:
        obj = json_list[dict]['objects']
        num += 1
        if num < 1600:
            continue
        # max_size = max(max_size, max(int(json_list[dict]['width']), int(json_list[dict]['height'])))
        # min_size = min(min_size, min(int(json_list[dict]['width']), int(json_list[dict]['height'])))
        if len(obj) == 0:
            img_path.append(rele_path + flag + '/' + dict)
            xmin_list.append('')
            ymin_list.append('')
            xmax_list.append('')
            ymax_list.append('')
            cate_list.append('')
        for key in obj:
            perObj = obj[key]
            img_path.append(rele_path + flag + '/' + dict)
            bbox = perObj['bbox']
            xmin_list.append(int(np.rint(bbox[0])))
            ymin_list.append(int(np.rint(bbox[1])))
            xmax_list.append(int(np.rint(bbox[2])))
            ymax_list.append(int(np.rint(bbox[3])))
            cate_list.append(perObj['category'])
            if flag == 'train':
                class_list[perObj['category']] = int(key)
        if num > 2400:
            print(num)
            break
    anno = pd.DataFrame()
    anno['img_path'] = img_path
    anno['xmin'] = xmin_list
    anno['ymin'] = ymin_list
    anno['xmax'] = xmax_list
    anno['ymax'] = ymax_list
    anno['category'] = cate_list
    anno.to_csv('../CSV/' + flag + 'n' + '_annotations.csv', index=None, header=None)

    json_file.close()
    print(flag + "存完了")
    print(len(class_list))


if __name__ == '__main__':
    # json_train_file = open('../CSV/train.json', 'r')
    json_val_file = open('../CSV/val.json', 'r')
    # json_to_csv(json_train_file, 'train')
    # csv_file = open('../CSV/classes.csv', 'w', newline='')
    # writer = csv.writer(csv_file)
    # class_list = dict(sorted(class_list.items(), key=lambda v: v[1]))
    # for item in class_list:
    #     writer.writerow([item, class_list[item]])
    # csv_file.close()
    json_to_csv(json_val_file, 'val')
