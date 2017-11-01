#!/bin/bash
#Delete log before 30 days

dir=/home/dsa/task/log/*
find $dir -mtime +30 -name "log*" -exec rm -f {} \;

