#!/bin/bash
dir=/home/d5000/jibei/var/QS/*
find $dir -mtime +85 -name "����_*" -exec rm -f {} \;
