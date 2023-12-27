# W-40 : 5.보안 관리 > 5.5 원격 시스템에서 강제로 시스템 종료

import subprocess
import re

def remote_shutdown():
    # 현재 사용자 권한 내보내기
    subprocess.run("Secedit /Export /Areas User_Rights /cfg c:\\privilege.inf", shell=True)

    # 파일 수정
    with open("privilege.inf", "r", encoding="utf-16") as file:
        lines = file.readlines()

    with open("privilege.inf", "w", encoding="utf-16") as file:
        for line in lines:
            if "SeRemoteShutdownPrivilege" in line:
                # 관리자 그룹(S-1-5-32-544)을 제외한 모든 SID 제거
                line = re.sub(r"(SeRemoteShutdownPrivilege\s*=\s*).*", r"\1*S-1-5-32-544,", line)
            file.write(line)

    # 수정된 설정 적용
    subprocess.run("secedit /configure /db C:\\Windows\\security\\local.sdb /cfg c:\\path\\filename.inf /areas USER_RIGHTS", shell=True)
    return True

def check_Privilege():
    # 보안 설정을 임시 파일로 내보내기
    subprocess.run("secedit /export /cfg C:\\tempsec.inf", shell=True)

    # 파일에서 SeRemoteShutdownPrivilege 값 찾기
    try:
        with open("C:\\tempsec.inf", "r") as file:
            contents = file.read()
            match = re.search(r"SeRemoteShutdownPrivilege\s*=\s*(.*)", contents)
            if match:
                # 관리자 그룹만 있는지 확인
                privileges = match.group(1).split(',')
                return privileges == ['*S-1-5-32-544']
            else:
                return False
    except FileNotFoundError:
        print("The security settings file could not be found.")
        return False

# 결과 확인
if remote_shutdown():
    print("remote shutdown privilege changed")

if check_Privilege():
    print("Now, Only the Administrator group has remote shutdown privilege.")
else:
    print("The remote shutdown is not set correctly or cannot be determined.")
