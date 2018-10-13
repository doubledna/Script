#!/bin/bash
#Delete log before 30 days

dir=/home/xxx/xxx/log/*
find $dir -mtime +30 -name "log*" -exec rm -f {} \;

