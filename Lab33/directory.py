import os
import shutil

directory = '/root/filesystem/home/ubuntu/labs/pro'
files = os.listdir(directory)
print("Files in Directory:", files)

destination = '/root/filesystem/home/ubuntu/labs/Lab33'
if not os.path.exists(destination):
    os.makedirs(destination)

for file in files:
    shutil.copy(os.path.join(directory, file), destination)
