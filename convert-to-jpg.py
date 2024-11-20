# A script that converts all HEIC files in a directory to JPG files

import os
import subprocess

# Get the current directory
current_directory = os.getcwd()

# Get all the files in the current directory
files = os.listdir(current_directory)

# Filter out all the HEIC files

heic_files = [file for file in files if file.endswith('.HEIC')]

# Convert all the HEIC files to JPG files

for heic_file in heic_files:
    jpg_file = heic_file.replace('.HEIC', '.jpg')
    command = f"sips -s format jpeg {heic_file} --out {jpg_file}"
    subprocess.run(command, shell=True)

print('All HEIC files have been converted to JPG files')

# End of script

