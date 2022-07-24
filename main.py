import os
import argparse
parser = argparse.ArgumentParser(description='')

parser.add_argument("-d",
                    "--dataset",
                    type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    myfile = open(args.dataset+'/sig.yaml', 'w+')
    myfile.write('train: {a}/images/train/\nval: {a}/images/valid/\n\nnc: 1\nnames: [\'tr\']'.format(a=args.dataset))

