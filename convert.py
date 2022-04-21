import os
import sys

def convert(directory):
    for subdir, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.stex'):
                print(f'converting file {file_name}')
                with open(os.path.join(subdir, file_name), 'rb') as in_file:
                    with open(os.path.join(subdir, file_name[:-5]+'.png'), 'wb') as out_file:
                        out_file.write(in_file.read()[32:])
                os.remove(os.path.join(subdir, file_name)) 

if __name__ == "__main__":
    if len(sys.argv) == 2:
        directory = sys.argv[1]
    else:
        directory = '.'
    print('Conver started!')
    convert(directory)
    if len(sys.argv) == 2:
        print('Converter finished!')
    else:
        input('Converter finished, press Enter to continue...')
