#!/bin/bash

# 프로젝트 디렉토리 내 모든 파일 목록 가져오기
files=$(find . -type f)

# Visual Studio Code에서 모든 파일 열기
for file in $files; do
    code -r "$file"
done