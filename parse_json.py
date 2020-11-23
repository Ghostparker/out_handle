import sys,os,cv2,json
import os.path as osp




def crop_only_onecar(resjson, save_dir):
    try:
        pass

    except:
        raise

def main():
    if(len(sys.argv) < 3):
        print('Please input jsonfile , picdir ')
        exit(1)
    else:
        jsonfile = sys.argv[1]
        pic_dir = sys.argv[2]
        save_dir = '/root/cutpic/{}'.format(pic_dir.split('/')[-1])

    if(osp.exists(save_dir) == False):
        os.makedirs(save_dir)

    for line in open(jsonfile):
        resjson = json.loads(line.strip())
        print(resjson)

        exit(1)






if __name__ == '__main__':
    main()