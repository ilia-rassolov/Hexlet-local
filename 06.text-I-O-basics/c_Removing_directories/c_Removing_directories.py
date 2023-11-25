import os

def rrmdir(directory_deleted):

    if not directory_deleted:
        return None
    print('directory_deleted = ', directory_deleted)

    if os.path.isfile(directory_deleted):
        print('file_del = ', directory_deleted)
        os.remove(directory_deleted)
        return None

    children = list(os.scandir(directory_deleted))
    print('children = ', children)

    if not children:
        print('dir-empty = ', directory_deleted)
        os.rmdir(directory_deleted)
        return None

    for child in children:
        if child:
            print('child = ', child)
            rrmdir(child)

    while directory_deleted:
        print('total_deleted = ', directory_deleted)
        rrmdir(directory_deleted)
        return None


rrmdir('dir-del')

