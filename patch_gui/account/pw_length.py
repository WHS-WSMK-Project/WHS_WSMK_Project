# W-49 : 1. 계정관리 > 1.10 패스워드 최소 암호 길이

import subprocess
import re

def change_pwlen():
    result = subprocess.run(["powershell", "-Command", "net accounts /MINPWLEN:8"], capture_output=True, text=True)
    return result.stdout

def check_pwlen():
    # net accounts의 출력 결과 output에 저장
    check_cmd = "net accounts"
    result = subprocess.run(["powershell", "-Command", check_cmd], capture_output=True, text=True)
    output = result.stdout

    # output중 패스워드 최소길이 항목이 8로 설정되었는지 확인
    if "Minimum password length" in output and "8" in output:
        return True
    else:
        return False