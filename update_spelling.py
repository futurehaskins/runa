#!python3

import os, re

def update_spellings(file_path, spelling_dict):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Replace spellings based on the dictionary
    for old_spelling, new_spelling in spelling_dict.items():
        text = re.sub(old_spelling, new_spelling, text)

    return text

def process_files(directory, spelling_dict):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('ON-YF.txt'):
                file_path = os.path.join(root, file)
                updated_text = update_spellings(file_path, spelling_dict)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(updated_text)

if __name__ == "__main__":
    # Your spelling dictionary
    spelling_dict = {
        'ᛒᚱᚢᚦᚱ': 'ᛒᚱᚢᚦᛦ',
        'ᚼᛅᚱᛒᛅᚱᚦᚱ': 'ᚼᚬᚱᛒᛅᚱᚦᛦ',
        'ᚴᚢᛅᛏ': 'ᚴᚢᛅᚦ',
        'ᚢᚴ': 'ᛅᚢᚴ',
        'ᚦᛁᛋ': 'ᚦᛅᛋ',
        'ᚢᚦᛁᚾ': 'ᚬᚦᛁᚾ',
        'ᛅᛏᛚᛁ': 'ᛅᛏᛚᛅ',
        'ᛋᛁᚦᛅᚾ': 'ᛋᛁᚦᚬᚾ',
        'ᛘᛅᛦ': 'ᛘᛅᚱ',
        'ᛁᚱ': 'ᛁᛋ',
        'ᛅᚾ': 'ᛁᚾ',
        'ᛅᚴ': 'ᛁᛅᚴ',
        'ᚢᛅᚱ': 'ᚢᛅᛦ',
        'ᚦᛁᚱ': 'ᚦᛁᛦ',
        'ᚴᛅᚦ': 'ᚴᛁᚦ',
        'ᚴᚬᛘᛦ': 'ᚴᚢᛘᛦ',
        'ᚴᛁᚠᛁᛏᚱ': 'ᚴᛁᚠᛁᛏᛦ',
        'ᚴᛁᛋᛏᚱ': 'ᚴᛁᛋᛏᛦ',
        'ᛒᚱᛅᚦᚱ': 'ᛒᚱᛅᚦᛦ',
        'ᛁᛏᚱᚦᛅᚴᚢ': 'ᛁᛏᛦᚦᛅᚴᚢ',
        'ᚢᛁᚱᚦᚱ': 'ᚢᛁᚱᚦᛦ',
        'ᛋᛁᛏᚱ': 'ᛋᛁᛏᛦ',
        'ᛘᛅᚦᚱ': 'ᛘᛅᚦᛦ',
        'ᚼᛁᛚᛏᚱ': 'ᚼᛁᛚᛏᛦ',
        'ᚼᚢᛁᚱ': 'ᚼᚢᛁᛦ',
        'ᚴᛁᛏᚱ': 'ᚴᛁᛏᛦ',
        'ᛒᛅᛏᚱᛁ': 'ᛒᛅᛏᛦᛁ',
        'ᛒᛁᛏᚱᛅ': 'ᛒᛁᛏᛦᛅ',
        'ᚢᛁᚱᛅ': 'ᚢᛁᛦᛅ',
        'ᚢᛁᚴᚱᛅ': 'ᚢᛁᚴᛦᛅ',
        'ᚠᚢᚱᛅ': 'ᚠᛅᛦᛅ',
        'ᚠᛚᛅᛁᚱ': 'ᚠᛚᛅᛁᛦᛅ',
        'ᚠᛁᛅᛏᚱᛅᚦᚱ': 'ᚠᛁᛅᛏᚱᛅᚦᛦ',
        'ᚴᛚᛅᚦᚱ': 'ᚴᛚᛅᚦᛦ',
        'ᚴᛅᛁᚱᛅᚱ': 'ᚴᛅᛁᚱᛅᛦ',
        'ᚴᛁᚱᛁ': 'ᚴᛅᛦᛁ',
        'ᚠᚢᛦ': 'ᚠᚬᛦ',
        'ᚦᛅ': 'ᚦᚬ',
        'ᚾᛅᛏᚱ': 'ᚾᚬᛏᛦ',
        'ᛘᚢᚦᚱ': 'ᛘᚢᚦᛦ',
        'ᛋᚢᛘ': 'ᛋᛁᛘ',
        'ᚠᚢᚱᛘᛅᛚᛁᛏᚱ': 'ᚠᚢᚱᛘᚬᛚᛁᛏᛦ',
        'ᛘᛅᛚᛁ': 'ᛘᚬᛚᛁ',
        'ᚠᚱᚢᚦᚱ': 'ᚠᚱᚢᚦᛦ',
        'ᛘᛅᛚᛁᛦ': 'ᛘᚬᛚᛁᛦ',
        'ᚼᚱᛅᚦᛘᛅᛚᛏ': 'ᚼᚱᛅᚦᛘᚬᛚᛏ',
        'ᚼᛅᛚᛏᛁᛏᚱ': 'ᚼᛅᛚᛏᛁᛏᛦ',
        'ᚠᛚᚢᛏᛅ': 'ᚠᛚᛅᛏᛅ',
        'ᛁᚱᚢᛋᚴ': 'ᛁᛦᚢᛋᚴ',
        'ᛚᛅᛏᚱ': 'ᛚᛅᛏᛦ',
        'ᛚᛅᛁᚦᚱ': 'ᛚᛅᛁᚦᛦ',
        'ᛏᚢᛅᚱ': 'ᛏᚢᛅᛦ',
        'ᛘᛅᛚ': 'ᛘᚬᛚ',
        'ᚠᚱᛅᛘᛅᚱ': 'ᚠᚱᛅᛘᛅᛦ',
        'ᚾᛅᛦ': 'ᚾᚬᛦ',
        'ᛘᛅᛏᛅᚱᚴᚢᚦᛅᚾ': 'ᛘᛅᛏᛅᛦ᛫ᚴᚢᚦᛅᚾ',
        'ᛘᛅᛏᛅᚱ': 'ᛘᛅᛏᛅᛦ',
        'ᚢᛅᚱᛁ': 'ᚢᛅᛦᛁ',
        'ᛋᚢᚾᛋᚴ': 'ᛋᚢᚾᛋᛏ',
        'ᚢᛁᚦᚱᚴᛁᚠᛁᛏᚱ': 'ᚢᛁᚦᛦᚴᛁᚠᛁᛏᛦ',
        'ᛁᛏᚱᚴᛁᚠᛁᛏᚱ': 'ᛁᛏᛦᚴᛁᚠᛁᛏᛦ',
        'ᛁᚱᚢᛋᚴ': 'ᛁᛦᚢᛋᚴ',
        'ᛒᛁᚦᚱ': 'ᛒᛁᚦᛦ',
        'ᚴᛅᚦᛁ': 'ᚴᛁᚦᛁ',
        'ᚦᛁᚱ': 'ᚦᛁᛦ',
        'ᛅᚴ': 'ᛁᚴ',
        'ᛋᛏᛁᛏᚱ': 'ᛋᛏᛅᛏᛦ',
        'ᚼᛚᚢᚱᛅᛏ': 'ᚼᛚᚢᛦ᛫ᛅᛏ',
        'ᚠᚱᛁᚦᚱ': 'ᚠᚱᛁᚦᛦ',
        'ᚬᚱᛚᛅᚴ': 'ᚢᛦᛚᛅᚴ',
        'ᛋᚢᚱᚴᛅᛚᛅᚢᛋᛅᛋᛏᚱ': 'ᛋᚢᚱᚴᛅᛚᛅᚢᛋᛅᛋᛏᛦ',
        'ᛒᚱᛅᚾ': 'ᛒᚱᛁᚾ',
        'ᚢᚾᛋᛏ': 'ᚢᛏᛋ',
        'ᚴᚢᚦᚱ': 'ᚴᚢᚦᛦ',
        'ᚢᚱᚴᛁᛏᚱ': 'ᚢᚱᚴᛁᛅᛏᛦ',
        'ᚾᛅᚠᚱᛅ': 'ᚾᚬᚠᛦᛅ',
        'ᚼᛅᛋᛏᛋ': 'ᚼᛁᛋᛏᛋ',
        'ᚠᚱᚢᚦᚱᛅ':'ᚠᚱᚢᚦᛦᛅ',
        'ᚼᚢᛅᛏᛅᛋᛏᚱ': 'ᚼᚢᛅᛏᛅᛋᛏᛦ',
        'ᛘᚢᛏᛁ': 'ᛘᚢᚾᛏᛁ',
        'ᛘᛅᛚᚢᚴᛁ': 'ᛘᚬᛚᚢᚴᛁ',
        'ᚼᛁᚴᛁ': 'ᚼᚾᚴᛁ',
        'ᛁᛚᛏᚱ': 'ᛁᛚᛏᛦ',
        'ᚾᛅᛁᛦ': 'ᚾᚬᛁᛦ',
        'ᚠᚱᛅᛏᚢᛘ': 'ᚠᚱᚬᛏᚢᛘ',
        'ᛁᛚᛁᚠᚦᚢᛘ': 'ᚢᛚᛁᚠᚦᚢᛘ',
        'ᛒᚱᛅᚾᛅ': 'ᛒᚱᛁᚾᛅ',
        'ᛏᛅᚢᚦᚱ': 'ᛏᛅᚢᚦᛦ',
        'ᚼᛅᛚᛏᚱ': 'ᚼᛅᛚᛏᛦ',
        'ᚱᛁᚦᚱ': 'ᚱᛁᚦᛦ',
        'ᚼᛅᛏᛅᚱᚢᛅᚾᛦ': 'ᚼᛅᛏᛅᛦᚢᛅᚾᛦ',
        'ᛒᛚᛁᛏᚱ': 'ᛒᛚᛁᛏᛦ',
        'ᛒᚱᛁᚾᛏᚱ': 'ᛒᚱᛁᚾᛏᛦ',
        'ᚾᛅᛋ': 'ᚾᚬᛋ',
        'ᛁᛒᛏᛁᛦ': 'ᛅᚠᛏᛁᛦ',
        'ᛒᛅᚢᛏᛅᚱᛋᛏᛅᛁᚾᛅᛦ': 'ᛒᛅᚢᛏᛅᛦᛋᛏᛅᛁᚾᛅᛦ',
        'ᚾᛁᚦᚱ': 'ᚾᛁᚦᛦ',
        'ᚼᛅᛏᛅᚱ': 'ᚼᛅᛏᛅᛦ',
        'ᚢᛅᚾᛁ': 'ᚢᚬᚾᛁ',
        'ᚾᚢᛏ': 'ᚾᚬᛏ',
        'ᚼᚢᛅᚱᚠ': 'ᚼᚢᛁᚱᛒ',
        'ᛘᛅᚾᛅᚦᛁ': 'ᛘᚬᚾᛅᚦᛁ',
        'ᚠᚱᛅᛏᚱ': 'ᚠᚱᚬᛏᛦ',
        'ᛅᛚᛏᚱᛅᛁ': 'ᛅᛚᛏᚱᛁ',
        'ᚴᚱᛁᛏᚱ': 'ᚴᚱᛁᛏᛦ',
        'ᚢᛅᚾᛅᛦ': 'ᚢᚬᚾᛅᛦ',
        'ᛅᚢᚦᚱ': 'ᛅᚢᚦᛦ'
    }

    # Replace spellings in ON-YF.txt files
    process_files('texts', spelling_dict)