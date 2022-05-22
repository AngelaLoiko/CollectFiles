import os
import ntpath
listfiles = {}
list_keys = []
file_result = 'MyFile.txt'
file_path = os.path.join(os.getcwd(), 'files')
file_result_path = os.path.join(file_path, file_result)
try:
    os.remove(file_result_path)       
except: FileNotFoundError


def dictfromdir (file_path):
    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            string = f'{ntpath.basename(file)}\n'       
            with open(os.path.join(file_path, file), 'r', encoding='utf-8') as f:         
               content = f.readlines()
               key_listfiles = len(content)
               string += f'{str(key_listfiles)}\n'
               for line in content:
                    string += line
               string += '\n'
               if key_listfiles in listfiles:
                    listfiles[key_listfiles] += [string]
               else:
                    listfiles[key_listfiles] = [string]
            print(listfiles)
    return listfiles

def filefromdict(file_path, file_result, listfiles):
    for k, v in listfiles.items():
        list_keys.append(k)
    list_keys.sort()

    with open(os.path.join(file_path, file_result), 'a+', encoding='utf-8') as f:
        for i in list_keys:
            for string in listfiles[i]:
                f.write(string)

dictfromdir(file_path)
filefromdict(file_path, file_result,listfiles)

print(f'Смотри изменения в файле {os.path.join(file_path, file_result)}')
           
           
           
           

