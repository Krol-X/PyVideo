import os, sys
s = os.path.split(sys.executable)[0]
os.system("pyinstaller --noupx -w --add-data icons;icons --add-binary %s/Lib/site-packages/cv2/opencv_videoio_ffmpeg420.dll;. -y -F -i PyVideo.ico -n PyVideo.exe __main__.py" % s)
os.system("pause")