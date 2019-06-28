import os
from glob import glob
from datetime import datetime

#対象とするディレクトリリストを取得
path = r'\\pluto\d(pluto)\●安全衛生\安全(大阪ｻｲﾄ)\交通\４８期'

#ディレクトリのみを取得する関数
def getdirs(path):
 dirs= []
 for item in os.listdir(path):
     if os.path.isdir(os.path.join(path,item)):
         dirs.append(item)
 return dirs

#検査対象ディレクトリリスト
directry_list = getdirs(path)
directry_list_num = len (directry_list)

#検査対象ファイルリスト（2次元）空の作成
file_lsit = [[] for i in range(directry_list_num)]

n = 0
for n in directry_list_num:
    for directry in directry_list:
        file_lsit[n].append(glob(os.path.join(path , directry)))

print (file_lsit)
