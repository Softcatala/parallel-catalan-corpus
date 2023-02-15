#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author Jordi Mas i Hernandez <jmas@softcatala.org>


import os
import fnmatch



def _find_recursive(directory, directory_pattern, pattern):
    filelist = []

    for root, dirs, files in os.walk(directory):
        for basename in files:
            if not fnmatch.fnmatch(root, directory_pattern):
                continue
            
            if not fnmatch.fnmatch(basename, pattern):
                continue
                
            filename = os.path.join(root, basename)
            filelist.append(filename)

    filelist.sort()
    return filelist

def _read_unique_sentences(filename, sentences_hash):
    added = 0
    duplicated = 0
    sentences = set()
    with open(filename, 'r') as tf:
        for line in tf.readlines():
            line = line.rstrip()
            line_hash = hash(line)
            if line_hash not in sentences_hash:
                sentences.add(line)
                sentences_hash.add(line_hash)
                added += 1
            else:
                duplicated += 1

    print(f"Processed file {filename} - added {added}, duplicated {duplicated}")
    return sentences

def _create_dir_if_does_exist(directory):
    if not os.path.exists(directory):
       os.makedirs(directory)

def main():

    print("Scans all languages and generates a monolingual Catalan corpus")

    OUTPUT_DIR = "monolingual"
    sentences_hash = set()
    strings = 0

    _create_dir_if_does_exist(OUTPUT_DIR)
    with open(f"{OUTPUT_DIR}/monolingual-catalan.txt", 'w') as tf:
        DIRECTORY_PATTERN = "*-cat*" # e.g 'eng-cat' directory
        FILE_PATTERN = "*.ca" # All the Catalan corpus end up with .ca extension
        for filename in _find_recursive(".", DIRECTORY_PATTERN, FILE_PATTERN):
            sentences = _read_unique_sentences(filename, sentences_hash)
            for sentence in sentences:
                tf.write(sentence + "\n")
                strings += 1

            del sentences

    print(f"Strings: {strings}")

if __name__ == "__main__":
    main()
