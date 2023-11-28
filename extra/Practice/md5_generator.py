import subprocess
import os

def generate_md5(directory="."):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory,file_name)
        if os.path.isfile(file_path):
            try:
                md5sum_output = subprocess.check_output(["md5sum",file_path],universal_newlines=True)
                md5_hash = md5sum_output.split()[0]
                print(f'File:{file_name} | MD5 hash : {md5_hash}')
            except subprocess.CalledProcessError as e:
                print(f"Error Calculating MD5 hash for {file_name} : {e}")
if __name__ == '__main__':
    generate_md5()