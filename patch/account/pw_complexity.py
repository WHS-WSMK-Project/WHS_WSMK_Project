# W-48 : 1. 계정관리 > 1.9 패스워드 복잡성 설정

import subprocess
import re

def change_pwcomplexity():
    subprocess.run('secedit /export /cfg C:\\winsec.inf', check=True, shell=True)
    try:
        with open("C:\\winsec.inf", 'r', encoding="utf-16") as file:
            data = file.read()
        pattern = r'PasswordComplexity\s*=\s*(\d)'
        match = re.search(pattern, data)

        if match and match.group(1) == '1':
            print("PasswordComplexity is already set to 1.")
            return False
        else:
            updated_data = re.sub(pattern, 'PasswordComplexity = 1', data)
            with open("C:\\winsec.inf", 'w', encoding="utf-16") as file:
                file.write(updated_data)
            subprocess.run('secedit /configure /db C:\\test.sdb /cfg C:\\winsec.inf /areas SECURITYPOLICY', shell=True)
            return True
    except IOError as e:
        print(f"File error: {e}")
        return False

def check_pwcomplexity():
    # 보안 설정을 임시 파일로 내보내기
    subprocess.run("secedit /export /cfg C:\\tempsec.inf", shell=True)

    # 파일에서 PasswordComplexity 값 찾기
    try:
        with open("C:\\tempsec.inf", "r", encoding="utf-16") as file:
            contents = file.read()
            match = re.search(r"PasswordComplexity\s*=\s*(\d+)", contents)
            if int(match.group(1)) == 1:
                return True
            else:
                return False
    except FileNotFoundError:
        print("The security settings file could not be found.")
        return False

# 결과 확인
if(change_pwcomplexity()):
    print("PasswordComplexity changed to 1")

if check_pwcomplexity():
    print("Password complexity is enabled.")
else:
    print("The password complexity is disabled or cannot be determined.")
