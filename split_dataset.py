import os
import argparse
import  shutil

parser = argparse.ArgumentParser(description='')

parser.add_argument("-l",
                    "--dataset_path",
                    type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    os.mkdir(args.dataset_path+'/dataset_long')
    os.mkdir(args.dataset_path + '/dataset_cross')
    os.mkdir(args.dataset_path + '/dataset_both')
    for root, dirs, files in os.walk(args.dataset_path):
        for file in files:
            print(os.path.join(root,file))
            if str(file).find('long')!=-1:
                shutil.copy(os.path.join(root,file), args.dataset_path+'/dataset_long/')
                shutil.copy(os.path.join(root,file), args.dataset_path + '/dataset_both/')
            if str(file).find('cross')!=-1:
                shutil.copy(os.path.join(root,file), args.dataset_path+'/dataset_cross/')
                shutil.copy(os.path.join(root,file), args.dataset_path + '/dataset_both/')

