import qrcode
import os
import sys

# qrコードの作成
img = qrcode.make(sys.argv[1])
# qrコードの保存パス
path = os.path.join(".","Seminar","python","files",sys.argv[2])
# qrコードの保存
img.save(path)