###Primarily to track images in my backup hdd but works for any archival data

import os
import hashlib
import sqlite3
import exifread
import json
from pathlib import Path

def create_checksum(file_path):
  with open(file_path, 'rb') as f:
    data = f.read()
    return hashlib.md5(data).hexdigest()
def check_datetime(file_path):
    with open(file_path, 'rb') as f:
          tags = exifread.process_file(f)
          #print(tags)
          # Extract the "Date Taken" metadata
          date_taken = tags.get('EXIF DateTimeOriginal', None)
          if date_taken is not None:
              return f'{date_taken}'
              print(f'{date_taken}')
          else:
              return 'NULL'
def grab_exif(file_path):
    with open(file_path, 'rb') as f:
        exif_data = exifread.process_file(f)
        if exif_data  is not None:
          return exif_data
        else:
            return 'NULL'
def write_checked(file_path,line):
    # Open the file in write mode
    with open(file_path, "a") as file:
        file.write(line + "\n")
def traverse_directory(root_dir, conn):
    cursor = conn.cursor()
    #get a text file of folders to skip
    file_path=os.path.join(folder_location,'toskip.txt')            
    # Open the file in read mode
    with open(file_path, 'r') as f:
        # Read all the lines in the file as a list
        lines = f.readlines()
    # Array of folder names to skip
    folders_to_skip = [line.rstrip() for line in lines]
    print(folders_to_skip)
    # Iterate over the files and directories in the current directory
    for root, dirs, files in os.walk(folder_location):
        if root in folders_to_skip:
            print(f'Skipping directory: {root}')
            continue
        else:
            file_count=len(files)
            print(f" This dir {root} has {file_count} of files")
            print(f"Processing dir: {root}")
            for file in files:
                #print(f"Processing file: {file}")
                file_path = os.path.join(root, file)
                #print(file_path)
                #checksum = create_checksum(file_path) more cpu intensive
                # Get the size of the file in bytes
                file_size = os.stat(file_path).st_size
                # Get the file name
                file_name = Path(file_path).name
                # Get the file extension
                _, fileFormat = os.path.splitext(file_name)
                #print(fileFormat)
                # Print the size and file name
                #print(f'Size: {file_size} bytes')
                #print(f'File Name: {file_name}')
                #extract datetime
                date_taken=''
                exif_data ={}
                if file_path.endswith(('.jpg', '.jpeg', '.JPG', '.JPEG', '.CR2', '.cr2')):
                    date_taken=check_datetime(file_path)
                #print(date_taken)
                cursor.execute('INSERT INTO checksums (fileFormat, file_path, file_name, file_size, date_taken) VALUES (?, ?, ?, ?, ?)', (fileFormat, file_path, file_name, file_size, date_taken))
            conn.commit()
            print(f'Checked {file_count} files in {root}')
            file_path = os.path.join(root, 'checked.txt')
            write_checked(file_path,root)

            
db_location = 'd:/imagedatabase.db'
folder_location = 'D:/recovered/'
conn = sqlite3.connect(db_location)
traverse_directory(folder_location, conn)
conn.close()
print("Completed checking the following")
