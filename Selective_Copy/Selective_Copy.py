import os, shutil
#todo walk throuth a folder tree
os.chdir('C:\\')
for foldername, subfolders , filenames in os.walk('C:\Python'):
    print('the current folder is ' + foldername)
    for subfolder in subfolders:
        print('subfolder of ' + foldername + ':' + subfolder)
    for filename in filenames:
        print('file inside ' + foldername + ':' + filename)
        #todo shearches for a file with a certain extension
        if filename.endswith('.txt') or filename.endswith('.docx') or filename.endswith('.doc'):
            print('this file is a text ' + filename)
        #todo copy these files from whatever they are into a new folder
            path =os.path.abspath(filename)
            print(path)
            str(path)
            shutil.copy(path,'C:\Python\Selective_Copy')

    print('')