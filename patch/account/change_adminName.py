# W-01 : 1. 계정관리 > 1.1 Administrator 계정 이름 변경 또는 보안성 강화

import subprocess

# Administrator 계정의 이름을 NewName으로 변경
def rename_administrator():
    command = f"wmic useraccount where name='Administrator' rename 'suan'"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result

# 변경된 계정 목록을 가져와서 확인
def check_exist():
    command = "wmic useraccount get name"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode().strip() 
    if "Administrator" in output:
        return False
    else:
        return True

# 확인 코드
print("Rename Result:", rename_administrator())

if check_exist():
    print("Account name successfully changed")
else:
    print("Account name change failed")
