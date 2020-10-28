import cv2
import os
# from os import listdir

def vid_frames(video_id = None, zip_name = None, basepath = None):
    vidcap = cv2.VideoCapture(f'{basepath}/{video_id}_.mp4')
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(f"{basepath}/{zip_name}/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        # print('Read a new frame: ', success)
        count += 1
    # print(f'Paths are >> {basepath}/{zip_name}.zip {basepath}/{zip_name}')
    os.system(f'zip -r {basepath}/{zip_name}.zip {basepath}/{zip_name}')
    print(f'Video id is >>> {video_id} and total frames extracted are >>> {count}')
