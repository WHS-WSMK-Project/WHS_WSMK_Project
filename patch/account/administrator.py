# W-01 : 1. 계정관리 > 1.1 Administrator 계정 이름 변경 또는 보안성 강화

import subprocess
import sys

def checkadname():
    result = subprocess.run(['powershell', 'Get-LocalUser Administrator | Select-Object -ExpandProperty Name'], capture_output=True, text=True)
    return result.stdout.strip()

def chadminame(newname):
    
    if checkadname() == "Administrator":
        subprocess.run(['powershell', f'Rename-LocalUser -Name "Administrator" -NewName "{newname}"'])
        print("Administrator name changed")  
    else:
        print("No User Named Administrator") 
        sys.exit()


# 결과 확인 코드
current_name = checkadname()
print(f"Administrator name: {current_name}")
chadminame("NewAdminName")
changed_name = checkadname()
print(f"changed Administrator name: {changed_name}")
