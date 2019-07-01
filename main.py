import os
from glob import glob
from datetime import datetime

#検査対象ディレクトリを入力
print ('検査対象のディレクトリパスを入力してください')
path = input()

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
file_list = [[] for i in range(directry_list_num)]

#検査対象ファイルリストの作成
for n in range(directry_list_num):
    for directry in directry_list:
        file_list[n].append(glob(os.path.join(path , (directry + '\*'))))

#検査対象ファイルリストの全ファイルの更新日時(エポック秒)を取得 ※datetime.fromtimestamp()でエポック秒をタイムスタンプに変換
#検査対象ファイルの更新時間リスト（空）の作成
updatetime_list = [[] for i in range(directry_list_num)]

#検査対象ファイルの更新時間リストの作成
for n in range(directry_list_num):
    for file_path in file_list[0][n]:
        updatetime_list[n].append(os.path.getctime(file_path))

#検査対象ファイルの更新時間リストそれぞれから最新更新時間を取得
#最新更新時間リスト（空）の作成
updatetime_new = []

#最新更新時間リストの作成
for n in range(directry_list_num):
    updatetime_new.append(max(updatetime_list[n]))

#最新更新時間リストのエポック秒を年/月/日 時間：分 に変換
updatetime_new_alt = []
for n in range(directry_list_num):
    updatetime_new_alt.append(datetime.fromtimestamp(updatetime_new[n]).strftime("%Y/%m/%d %H:%M"))

#検査対象ディレクトリ名リストと最新更新時間リストをマージ
updatetime_dir = [[] for i in range(directry_list_num)]

for n in range(directry_list_num):
    updatetime_dir[n].append(directry_list[n])
    updatetime_dir[n].append(updatetime_new_alt[n])

#検査対象ディレクトリの最新更新時間リストを出力
for n in range(directry_list_num):
    print ('対象：' + updatetime_dir[n][0] + ' 更新時間：' + updatetime_dir[n][1])
