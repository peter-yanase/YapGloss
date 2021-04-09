# YapGloss v. 1.3
# By Peter Yanase, PhD.
# Last updated on 7/4/2021
# License : GPLv3

import os
import csv
import docx2txt

def no_folder(folder):
    if not os.path.exists(folder):
        print('Folder not found:', folder)
        quit()

def build_glossary(source_file_stem):
    with open((os.path.join(target_folder, source_file_stem) + '_glossary.md'), 'w') as output_file:
        output_file.write('# Glossary：\n\n')
        for source_language, target_language in dictionary_entries.items():
            if source_language in source_text:
                output_file.write('- %s %s\n' % (source_language, target_language))
    print("Finished building glossary for", file_name)

source_folder = 'source'
no_folder(source_folder)
target_folder = 'target'
no_folder(target_folder)
dictionary_folder = 'dictionaries'
no_folder(dictionary_folder)

dictionary_entries = {}
for file_name in os.listdir(dictionary_folder):
    split_file_name = os.path.splitext(file_name)
    if split_file_name[1] == '.csv':
        dictionary = csv.reader(open(os.path.join(dictionary_folder, file_name)))
        dictionary_entries.update({row[0]: row[1] for row in dictionary})

for file_name in os.listdir(source_folder):
    split_file_name = os.path.splitext(file_name)
    if split_file_name[1] == '.txt':
        source_text = open(os.path.join(source_folder, file_name)).read()
        build_glossary(split_file_name[0])
    elif os.path.splitext(file_name)[1] == '.docx':
        source_text = docx2txt.process(os.path.join(source_folder, file_name))
        build_glossary(split_file_name[0])
