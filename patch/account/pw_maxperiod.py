# W-50 : 1. 계정관리 > 1.11 패스워드 최대 사용 기간

import subprocess
import re

def change_maxperiod():
    result = subprocess.run(["powershell", "-Command", "net accounts /MAXPWAGE:30"], capture_output=True, text=True)
    return result.stdout

def check_maxperiod():
    # net accounts의 출력 결과 output에 저장
    check_cmd = "net accounts"
    result = subprocess.run(["powershell", "-Command", check_cmd], capture_output=True, text=True)
    output = result.stdout

    # output중 패스워드 최대 사용기간이 30로 설정되었는지 확인
    if "Maximum password age (days)" in output and "30" in output:
        return True
    else:
        return False

# 결과 확인
check_cmd = "net accounts"
result = subprocess.run(["powershell", "-Command", check_cmd], capture_output=True, text=True)
output = result.stdout
match = re.search(r"Maximum password age \(days\):\s+(\d+)", output)

changed = check_maxperiod()

print("Command Execution Output:", change_maxperiod())
print("Maximum password age Changed:", changed)
print("Password Policy Check Output:", match.group(0))
