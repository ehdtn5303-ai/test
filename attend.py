# attend.py
import os

filename = "attendance.txt"

print("--- 스터디 출석부 ---")
name = input("이름을 입력하세요: ")
date = input("날짜를 입력하세요 (예: 2024-05-20): ")

# 파일에 저장 (추가 모드 'a')
with open(filename, "a", encoding="utf-8") as f:
    f.write(f"{date} : {name}\n")

print("\n[현재 출석 명단]")
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())