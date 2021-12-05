import os
import shutil

source = 'C:\\Users\\tigju\\Desktop\\api'
destination = 'C:\\Users\\tigju\\Documents\\ineuron\\python_basic_assignmemt\\new'

def include_patterns(pattern):
    '''
    pass the list of extentions which want to keep
    '''
    all_ext = set()
    new_pat = tuple(pattern)
    for file in os.listdir(source):
        if file.endswith(new_pat):
            continue
        else:
            file_ext = os.path.splitext(file)[1]
            all_ext.add(file_ext)
    
    rem_ext = ["*" + ext if len(ext) > 0 else ext for ext in all_ext]
    return rem_ext


if __name__ == "__main__":

    rem_ext = include_patterns(['.txt', '.JPG'])
    print(rem_ext)


    # mylst = set()
    # for file in os.listdir(source):
    #     if file.endswith('.txt') or file.endswith('.JPG'):
    #         continue
    #     else:
    #         file_ext = os.path.splitext(file)[1]
    #         # if len(file_ext) > 0:
    #         mylst.add(file_ext)

    # new_list = ["*"+ ext if len(ext) > 0 else ext for ext in mylst]    

    # print(new_list)

    shutil.copytree(source, destination, ignore=shutil.ignore_patterns(*rem_ext))
