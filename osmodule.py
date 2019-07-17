import os
# from datetime import datetime

os.chdir('/Users/byronmartinez/Dropbox/dev/python/pytut/')

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'testy.txt')

print(dir(os.path))

# walk_path = '/Users/byronmartinez/Dropbox/dev/'

# for dirpath, dirnames, filenames in os.walk(walk_path):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

# os.mkdir('OS-Demo-2/Sub-Dir-1')
# os.makedirs('OS-Demo-2/Sub-Dir-1')

# os.rmdir('OS-Demo-2/Sub-Dir-1')
# os.removedirs('OS-Demo-2/Sub-Dir-1')

# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# with open('test.txt', 'w') as rf:
#     pass

# print(os.listdir())
