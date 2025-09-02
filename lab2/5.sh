#!/bin/bash

# 获取所有以 python 开头的进程（不区分大小写），提取用户名，去重并计数
count=$(ps aux | grep -i '^[^ ]* *[^ ]* *[^ ]* *[^ ]* *[^ ]* *[^ ]* *[^ ]* *python' | awk '{print $1}' | sort | uniq | wc -l)

# 如果计数为0，输出0；否则输出用户数
if [ "$count" -eq 0 ]; then
    echo "0"
else
    echo "$count"
fi
