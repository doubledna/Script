#!/bin/bash
dir=/home/d5000/jibei/var/QS/*
find $dir -mtime +85 -name "¹úµ÷_*" -exec rm -f {} \;
