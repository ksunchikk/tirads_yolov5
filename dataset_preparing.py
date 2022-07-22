import pandas as pd
import os
import argparse
import  shutil

parser = argparse.ArgumentParser(description='Great Description To Be Here')

parser.add_argument("-c",
                    "--csv_path",
                    type=str)
parser.add_argument("-l",
                    "--labels_path",
                    type=str)

def from_csv_to_txt(file_path, labels_path):
    dataFrame = pd.read_csv(file_path)
    pt = 'C:/Users/ksesh/yolov5_tirads/dataset/images/'
    for a1, row in dataFrame.iterrows():
        # o_path = row.image_path
        l_path = row.image_label_path[::-1]
        # l_path = pt + l_path
        # print(o_path)
        # print(l_path)
        # shutil.copyfile(o_path, l_path)
        # #os.popen('copy {first} {second}'.format(first=o_path, second = l_path))
        l_path = l_path[10:]
        l_path = l_path[::-1]
        new_file = open(l_path+'.txt', 'w+')
        print(l_path)
        x_center = int((int(row.right) + int(row.left))/2)/row.width
        y_center = int((int(row['down']) + int(row['up']))/2)/row['height']
        width = (int(row['right']) - int(row['left']))/row['width']
        height = (int(row['down']) - int(row['up']))/row['height']
        new_file.write('0 '+str(x_center) + " "+ str(y_center)+" "+str(width)+" "+ str(height))
        new_file.close()

if __name__ == '__main__':
    args = parser.parse_args()
    from_csv_to_txt(args.csv_path, args.labels_path)