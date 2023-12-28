# W-16 : 2. 서비스관리 > 2.10 IIS 링크 사용 금지

import subprocess
import sys

def disable_directory_browsing():
    # PowerShell 명령어
    powershell_command = '''
    Set-WebConfigurationProperty -Filter '/system.webServer/directoryBrowse' -PSPath 'IIS:\' -Name enabled -Value $false
    '''

    # PowerShell 명령어 실행
    result = subprocess.run(['powershell', '-Command', powershell_command], capture_output=True, text=True)

    # 실행 결과 확인
    if result.returncode == 0:
        print("Disabled successfully")
    else:
        print("Failed to disable")
        print(result.stderr)
        sys.exit()

# 디렉터리 브라우징 비활성화 함수 호출
disable_directory_browsing()
