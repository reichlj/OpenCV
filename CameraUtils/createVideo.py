import sys
import os
import cv2

# Logitech 930e - Resolutions supported:
#  160x120 , 176x144 , 320x180 , 320x240 , 352x288 , 424x240 , 480x270
#  640x360 , 640x480 , 800x448 , 800x600 , 848x480 , 960x540
#  1024x576 , 1280x720 , 1600x896 , 1920x1080

def setVideoCaptureSize(cap, resolution):
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution['height']);
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution['width']);

def saveFirstFrame(frame,path,name):
    img_name = name + '_first' + '.jpg'
    cv2.imwrite(os.path.join(path, img_name),frame)

def checkVideoCaptureSize(cap, resolution):
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    if height != resolution['height'] or width != resolution['width']:
        print('Resolution width={0:5d} height={1:5d} not supported!'.format(
                   resolution['width'], resolution['height']))
        print('  Height: found={0:5d} expected={1:5d}'.format(height, resolution['height']))
        print('  Width : found={0:5d} expected={1:5d}'.format(width, resolution['width']))
        return False
    else:
        return True

def start_and_stop_listener(event,x,y,flags, params):
    global is_capturing, stop_capturing
    if event == cv2.EVENT_LBUTTONDOWN:
        if is_capturing is False:
            is_capturing = True
            print('Capturing started.')
            return
        if is_capturing is True:
            stop_capturing = True
            print('Capturing stopped.')


resolution = {'width': 640, 'height': 480}
path = 'videos'
name = 'trackZuendis'
video_path_name = os.path.join(path, name + '.avi')

print('Click on Frame to start and stops capturing!')
print('Resolution ({0:d},{1:d})'.format(resolution['width'],resolution['height']))
print('Video is stored at',os.path.abspath(video_path_name))

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
setVideoCaptureSize(cap, resolution)
if not checkVideoCaptureSize(cap,resolution):
    sys.exit(0)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(video_path_name,fourcc, 25,(resolution['width'],resolution['height']))

is_capturing = False
stop_capturing = False
first = True
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', start_and_stop_listener)

while True:
    ret, frame = cap.read()
    if ret is False:
        print('Error during capture - ret ' + str(ret))
        break
    cv2.imshow('Frame',frame)
    if is_capturing:
        if first:
            saveFirstFrame(frame,path,name)
            first = False
        out.write(frame)
        if stop_capturing:
            break
    key = cv2.waitKey(25)
    if key == 27:
        break

out.release()
cap.release()
cv2.destroyAllWindows()
print('Program completed')