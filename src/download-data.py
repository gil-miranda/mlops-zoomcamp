## This is a work in progress
import yaml
import requests
import os

with open(r'config.yml') as file:
    CONFIG = yaml.safe_load(file)

def check_folders():
    folder_exists = os.path.isdir(CONFIG['datasets']['folder'])
    if not folder_exists:
        create_folders()
    return folder_exists

def create_folders():
    os.mkdir('data')
    os.mkdir(CONFIG['datasets']['folder'])
    return None

def download_data(section='section-01'):
    for ds in CONFIG['datasets'][section]:
        for _,f in CONFIG['datasets'][section][ds].items():
            response = requests.get(f)
            file_name = f.split('/')[-1]
            open(f"{CONFIG['datasets']['folder']}/{file_name}", 'wb').write(response.content)

if __name__ == '__main__':
    check_folders()
    download_data()
