import os

def rename_files():
    #list all the contents of folders
    file_list = os.listdir(r'/Users/Raghav/Desktop/Nanodegree/prank')
    print(file_list);
    saved_path = os.getcwd()
    print(saved_path)

    os.chdir(r'/Users/Raghav/Desktop/Nanodegree/prank')
    #Rename file name
    for file_name in file_list:
        print(file_name+" This is name")
        os.rename(file_name, file_name.translate(None, "0123456789"))


rename_files()
