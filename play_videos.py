import cv2
import os
import sys

def play_video(out_dir,path,jump_size=1):

    cap = cv2.VideoCapture(path)

    #check if the video capture is open
    if(cap.isOpened() == False):
        print("Error Opening Video Stream Or File {}".format(path))
        return

    frame_ind = 0
    viedo_name = os.path.split(path)[1].split('.')[0]
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    while(cap.isOpened()):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_ind)
        ret, frame = cap.read()
        if ret == False:
            break
        frame_name='frame {} out_off {}'.format(frame_ind, total)
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.setWindowTitle('frame',frame_name)
        cv2.imshow('frame', frame)


        key = cv2.waitKey(0)

        if key  == ord('n'):
            frame_ind +=jump_size
            if frame_ind >= total-1:
                frame_ind  = total-1

        elif key  == ord('b'):
            frame_ind -=jump_size
            if frame_ind<0:
                frame_ind  = 0

        elif key == ord('s'):
            os.makedirs(os.path.join(out_dir,viedo_name.replace(' ','_')),exist_ok=True)
            dst_path = os.path.join(out_dir,viedo_name.replace(' ','_'),str(frame_ind)+'_color.png')
            cv2.imwrite(dst_path,frame)
            frame_ind += jump_size

        elif key == ord('q'):
            break




        cv2.imshow('frame', frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    jump_size = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    for root,subdir,files in os.walk(sys.argv[1]):
        for file in files:
            play_video(sys.argv[2], os.path.join(root,file),jump_size)



