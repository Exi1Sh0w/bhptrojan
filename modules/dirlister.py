import os

def run(**kwargs):
    '''
    列出当前目录下所有的文件
    '''
    print("[*] In dirlister module")
    files = os.listdir('.')
    return str(files)