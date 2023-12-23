# W-40 : 5.보안 관리 > 5.5 원격 시스템에서 강제로 시스템 종료

import subprocess
import re

def remote_shutdown():
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
    print("Now, Only the Administrator group has remote shutdown privilege.")
else:
    print("The remote shutdown is not set correctly or cannot be determined.")
