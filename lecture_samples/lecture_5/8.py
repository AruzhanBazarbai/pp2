import os
import shutil
src="/Users/Асер/Documents/pp2/lecture_samples/informatics/tasks1/"
dst="/Users/Асер/Documents/pp2/lecture_samples/informatics/tasks11/"
#shutil.move(src,dst)// скопирует
shutil.copytree(src,dst) #создает точно такую же папку и копирует туда все из этого файла
#copy-скопирует файла
shutil.rmtree(src)
print(os.listdir(dst))