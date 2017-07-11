#!/bin/bash


echo "shell.sh $1 $2"


apktool=($(apktool d "$1" -o "$2"))
echo ${apktool[@]}

