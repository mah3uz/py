# Rename files
import os
os.chdir('/home/mahfuz/Desktop/_files')
for file in os.listdir():
    ext = '.txt'
    f_name, f_num = file.split('_')
    new_name = f'{f_num.zfill(3)} - {f_name}{ext}'
    
    os.rename(file, new_name)