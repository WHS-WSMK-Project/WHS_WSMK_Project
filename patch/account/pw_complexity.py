# W-48 : 1. 계정관리 > 1.9 패스워드 복잡성 설정

import subprocess
import re

def check_pwcomplexity():
    # 보안 설정을 임시 파일로 내보내기
    subprocess.run("secedit /export /cfg C:\\tempsec.inf", shell=True)

    # 파일에서 PasswordComplexity 값 찾기
    try:
        with open("C:\\tempsec.inf", "r") as file:
            contents = file.read()
            match = re.search(r"PasswordComplexity\s*=\s*(\d+)", contents)
            if match:
                return int(match.group(1)) == 1
            else:
                return False
    except FileNotFoundError:
        print("The security settings file could not be found.")
        return False

# 결과 확인
if check_pwcomplexity():
    print("Password complexity is enabled.")
else:
    print("The password complexity is disabled or cannot be determined.")
