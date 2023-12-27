import subprocess
import sys

def set_limit(limit_bytes):
		#파워쉘 명령어 생성해서 업로드 및 다운로드 크기 제한을 설정
    powershell_command = f'Set-WebConfiguration -Filter "/system.webServer/security/requestFiltering/requestLimits" -PSPath "IIS:" -Value @{{maxAllowedContentLength = {limit_bytes}}}'
    result = subprocess.run(['powershell', powershell_command], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Upload and download limit set to {limit_bytes} bytes")
    else:
        print("Failed to set upload and download limit")
        print(result.stderr)
        sys.exit()

# 업로드 및 다운로드 크기 제한을 1MB로 설정
limit_bytes(1048576)

# 결과 확인
print(f"Current upload and download limit: {current_limit} bytes")
set_limit(limit_bytes)
