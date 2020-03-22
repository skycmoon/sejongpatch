#!/usr/bin/env bash
SOURCE_FOLDER=$1
TARGET_FOLDER=$2

for i in $(ls ${SOURCE_FOLDER}/*.txt); do dos2unix ${i}; done
for i in $(ls ${SOURCE_FOLDER}/*.txt); do python3 main.py --input ${i} --output ${TARGET_FOLDER}/$(basename ${i}); done
