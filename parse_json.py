import sys,os,cv2,json
import os.path as osp
import numpy as np
detname = ['car','person','bicycle','tricycle']


def crop_only_onecar(resjson, save_dir,ori_dir):
    try:
        fn = resjson['url_image']

        print(save_dir)
        picfn = osp.join(ori_dir,'{}'.format(fn.split('/')[-1]))
        src = cv2.imread(picfn)

        res = resjson['result']
        # print('--------------')


        dt = None
        for i in res:
            if(i['tagtype'] in detname):
                dt = i['data']
                break
        x1,y1,w,h = dt
        x2,y2 = x1+w,y1+h

        blackpic = np.zeros_like(src)
        # print(blackpic.shape)
        blackpic[y1:y2,x1:x2,] = src[y1:y2,x1:x2,]
        writefn = osp.join(save_dir,fn.split('/')[-1])
        cv2.imwrite(writefn,blackpic)

    except:
        raise

def main():
    if(len(sys.argv) < 3):
        print('Please input jsonfile , picdir ')
        exit(1)
    else:
        jsonfile = sys.argv[1]
        pic_dir = sys.argv[2]
        print(pic_dir)
        data = pic_dir.split('/')
        save_dir = '/root/cutpic/{}/{}'.format(data[-2],data[-1])

    if(osp.exists(save_dir) == False):
        os.makedirs(save_dir)

    for line in open(jsonfile):
        resjson = json.loads(line.strip())
        # print(resjson)
        crop_only_onecar(resjson,save_dir,pic_dir)
        exit(1)






if __name__ == '__main__':
    main()