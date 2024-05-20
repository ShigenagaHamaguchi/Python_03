import os
import sys
import qrcode   #パッケージをインポート

args = sys.argv
url = args[1]   
png = args[2]   

#QRコードを生成
img = qrcode.make(url)

#相対パスの生成
path = os.path.join(".", "files", png)

#ファイルに保存
img.save(path)