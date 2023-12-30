# W-17 : 2. 서비스관리 > 2.11 IIS 파일 업로드 및 다운로드 제한

import subprocess
import sys

def set_limit(limit_bytes):
    powershell_command = f'Set-WebConfiguration -Filter "/system.webServer/security/requestFiltering/requestLimits" -PSPath "IIS:" -Value @{{maxAllowedContentLength = {limit_bytes}}}'
    result = subprocess.run(['powershell', powershell_command], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Upload and download limits are set to {limit_bytes} bytes.")
        return True
    else:
        print("setting upload and download failed")
        return False