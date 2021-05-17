import cv2
import sys

# Logitech 930e - Resolutions supported:
#  160x120 , 176x144 , 320x180 , 320x240 , 352x288 , 424x240 , 480x270
#  640x360 , 640x480 , 800x448 , 800x600 , 848x480 , 960x540
#  1024x576 , 1280x720 , 1600x896 , 1920x1080

def setVideoCaptureSize(cap, resolution):
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution['height']);
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution['width']);

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

print('Set and test a given resolution')

#resolution = {'width': 1920, 'height': 1080}
resolution = {'width': 801, 'height': 600}
#resolution = {'width': -1, 'height': -1}  # set default resolution

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
setVideoCaptureSize(cap, resolution)
if not checkVideoCaptureSize(cap,resolution):
    sys.exit(0)

try:
    ret, image = cap.read()
    if ret:
        if resolution['height'] == -1 and resolution['width'] == -1:
            title = 'Default Resolution, Image found: (w={0:d},h={1:d}) '.format(
                image.shape[1], image.shape[0])
        else:
            title = 'Resolution set: (w={0:d},h={1:d}) Image found: (w={2:d},h={3:d}) '.format(
                resolution['width'], resolution['height'], image.shape[1], image.shape[0])

        cv2.imshow(title,image)
        cv2.waitKey(0)
except Exception as ex:
    print(ex)

cap.release()
cv2.destroyAllWindows()