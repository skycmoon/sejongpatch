#!/usr/bin/env bash
SOURCE=$1
TARGET=$2

for i in $(ls ${SOURCE}/*.txt); do dos2unix ${i}; done
for i in $(ls ${SOURCE}/*.txt); do sed "s/\\/NA/\\/ZZ/g" ${i} > ${TARGET}/$(basename ${i}); done
for i in $(ls ${SOURCE}/*.txt); do  ${i}; done