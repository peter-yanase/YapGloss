# YapGloss
A Python script for translators. It looks through your text files and automatically builds glossaries for them.

## How it works

The programm takes your csv files and merges them into a single list first then goes through the entries one after another and checks if they can be found in your source texts. Finally, it prints out a list of the words for separate markdown files.

## How to install

1. Download and copy yapgloss.py into an empty folder.
2. Make the following three folders inside the same folder:
  - source
  - target
  - dictionary
3. Copy your glossaries into the dictionary folder. Note, the files must be in csv format. The first column must be the entry in the source language while the second the entry for the target language.
4. Copy the source texts into the source folder. Note, the files must be in txt or docx formats.
5. Run the program.
