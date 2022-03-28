import os
import sys
import cv2
import multiprocessing
import time


def process_file(root,file):
    if '_color.png' in file:
        return
    name = os.path.join(root, file)
    im = cv2.imread(name)
    if im is None:
        return
    os.remove(name)
    if name.endswith('_color.png') == True:
        return
    ext = os.path.splitext(name)[1]
    name = name.replace(ext,'_color.png')
    cv2.imwrite(name,im)

if __name__ == '__main__':
    for root, subdirs, files in os.walk(sys.argv[1]):
        for file in files:
            while len(multiprocessing.active_children()) > multiprocessing.cpu_count() -2:
                time.sleep(0.1)
            p = multiprocessing.Process(target=process_file, args=(root,file))
            p.start()
