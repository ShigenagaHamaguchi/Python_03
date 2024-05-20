import sys
import qrcode
import os

url = sys.argv[1]
file_name = sys.argv[2]

path = os.path.join("..", "..","files","{}.png".format(file_name))

img = qrcode.make(url)
img.save(path)

