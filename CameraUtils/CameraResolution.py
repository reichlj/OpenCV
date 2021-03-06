import pandas as pd
import cv2
# Logitech 930e - Resolutions supported:
#  160x120 , 176x144 , 320x180 , 320x240 , 352x288 , 424x240 , 480x270
#  640x360 , 640x480 , 800x448 , 800x600 , 848x480 , 960x540
#  1024x576 , 1280x720 , 1600x896 , 1920x1080

# get the default capture resolution
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Default Capture Resolution: (Width={0:d},Height={1:d})'.format(width,height))

# find all capture resolutions supported by the camera
# url contains table of almost all resolutions known
url = "https://en.wikipedia.org/wiki/List_of_common_resolutions"
table = pd.read_html(url)[0]
table.columns = table.columns.droplevel()

resolutions = {}

for index, row in table[["W", "H"]].iterrows():
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, row["W"])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, row["H"])
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    resolutions[ width,height ] = "OK"
    print('{0:3d} w_set={1:4d} h_set={2:4d} w_get={3:4d} h_get={4:4d}'.format(
          index,row["W"],row["H"],width,height))
cap.release()

print('Capture Resolutions (Width x Height) supported by the camera:')
# sort by width
for count, item in enumerate(sorted(resolutions.keys(), key=lambda x: x[0])):
    print(' {0:d}x{1:d} ,'.format(*item), end='')
    if (count+1)%7 == 0:
        print('')
print('\nEnde')
