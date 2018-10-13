#!/bin/bash
dir=/home/d5000/xxx/xxx/*
find $dir -mtime +85 -name "xxx" -exec rm -f {} \;
