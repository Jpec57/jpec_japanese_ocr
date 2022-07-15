import os
from os import listdir
from os.path import isfile
import shutil
import csv


def get_utf8_char_from_hex_unicode(hex_str):
    return chr(int(hex_str, 16))


BASE_DATA_PATH = "etl_data/"
BASE_IMG_PATH = "etl_data/images/"
BASE_IMG_OUTPUT_PATH = "final_data/char_images/"

data_collection_folders = [
    'ETL1',
    'ETL2',
    'ETL3',
    'ETL4',
    'ETL5',
    'ETL6',
    'ETL7',
    'ETL8B',
    'ETL8G',
    'ETL9B',
    'ETL9G'
]

if not os.path.exists(BASE_IMG_OUTPUT_PATH):
    os.makedirs(BASE_IMG_OUTPUT_PATH, mode=0o777)

header = ['character', 'filepath', 'source']

with open('final_data/japanese_characters.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f, escapechar='\\')
    writer.writerow(header)

    for data_folder in data_collection_folders:
        if os.path.exists(BASE_IMG_PATH + data_folder):
            for hex_char_name in listdir(BASE_IMG_PATH + data_folder):
                if isfile(hex_char_name):
                    print("Ignoring file", hex_char_name)
                    continue
                if not os.path.exists(BASE_IMG_OUTPUT_PATH + hex_char_name):
                    os.makedirs(BASE_IMG_OUTPUT_PATH +
                                hex_char_name, mode=0o777)
                for img in listdir(BASE_IMG_PATH + data_folder + '/' + hex_char_name):
                    if img.endswith(".png"):
                        prev_path = BASE_IMG_PATH + data_folder + '/' + hex_char_name + '/' + img
                        new_path = BASE_IMG_OUTPUT_PATH + hex_char_name + '/' + data_folder.lower() + \
                            '_' + img
                        # print("Moving file", prev_path, 'to', new_path)
                        shutil.move(prev_path, new_path)
                        char = get_utf8_char_from_hex_unicode(hex_char_name)
                        writer.writerow([char, new_path, data_folder])
