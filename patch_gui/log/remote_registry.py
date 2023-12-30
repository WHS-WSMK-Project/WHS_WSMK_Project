# W-35 : 4. 로그관리 > 4.2 Remote Registry Control

import subprocess

def check_status():
    # RemoteRegistry 상태 확인
    result = subprocess.run(['reg', 'query', 'HKLM\SYSTEM\CurrentControlSet\Services\RemoteRegistry', '/v', 'Start'], capture_output=True, text=True)
    
    # 결과에서 REG_DWORD 부분 추출
    start_value = None
    if "REG_DWORD" in result.stdout:
        start_value = result.stdout.split("REG_DWORD")[1].strip()

    return start_value

def disable_remote_registry():
    # RemoteRegistry 상태 확인
    start_value = check_status()

    # RemoteRegistry를 사용 안함으로 변경
    if start_value and start_value != "0x4":
        subprocess.run(['reg', 'add', 'HKLM\SYSTEM\CurrentControlSet\Services\RemoteRegistry', '/v', 'Start', '/t', 'REG_DWORD', '/d', '4', '/f'])
        print("RemoteRegistry has been changed to disabled.")
        return True
    else:
        print("RemoteRegistry is already disabled.")
        return False
    