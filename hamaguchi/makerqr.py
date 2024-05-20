import qrcode
import os
import sys



img = qrcode.make(sys.argv[1])
path = os.path.join(".","Seminar","python","files",sys.argv[2])
img.save(path)