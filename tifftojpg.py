import os
import re

import cv2 as cv
import argparse
import tifffile as tiff
from PIL import Image, ImageEnhance

parser = argparse.ArgumentParser(description='Great Description To Be Here')

parser.add_argument("-s",
                    "--source_path",
                    type=str)
parser.add_argument("-o",
                    "--out_path",
                    type=str)


def parseDirs(src, dst):
        imgs = os.listdir(src)
        for j in imgs:
            res = re.findall('mask', j)
            l = len(res)
            temp = convert(src + '/' + j)
            if l == 0:
                tmp = j[::-1]
                tmp = tmp[4:]
                tmp = tmp[::-1]
                for index, item in enumerate(temp):
                    path = dst + '/images/' + tmp + '_' + str(index) + '.jpg'
                    print(path)
                    cv.imwrite(path, item)
                    im = Image.open(path)
                    ench1 = ImageEnhance.Contrast(im)
                    im = ench1.enhance(1.5)
                    im.save(path)
            else:
                tmp = j[::-1]
                tmp = tmp[9:]
                tmp = tmp[::-1]
                for index, item in enumerate(temp):
                    item = cv.convertScaleAbs(item, alpha=255.0)
                    path = dst + '/labels/' + tmp + '_' + str(index) + '_' + 'label' + '.jpg'
                    print(path)
                    cv.imwrite(path, item)


def convert(img):
    tmp = []
    temp = tiff.imread(img)
    for img in temp:
        shape = img.shape
        if shape == (735, 975):
            img = img[100:700, 0:900]
        if shape == (735, 975, 3):
            img = img[100:700, 0:900]
        img = cv.resize(img, (768, 768))
        tmp.append(img)
    return tmp


def main(_):
    parseDirs(args.source_path, args.out_path)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
