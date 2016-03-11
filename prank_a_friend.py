def prank_files():
    import os
    files_list=os.listdir("C:\Users\IBM_ADMIN\Pictures\prank\prank")
    print files_list
    saved_path=os.getcwd()
    print saved_path

    os.chdir("C:\Users\IBM_ADMIN\Pictures\prank\prank")
    
    for file_name in files_list:
        os.rename(file_name,file_name.translate(None,'0123456789'))
