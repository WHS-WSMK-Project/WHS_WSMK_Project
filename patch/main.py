import subprocess
import re

# 1. 계정 관리
from patch.account import change_adminName
from patch.account import pw_complexity
from patch.account import pw_length
from patch.account import pw_maxperiod

# 2. 서비스 관리
from patch.service import disable_link
from patch.service import limit_upload_download
from patch.service import remove_mapping
from patch.service import disable_WebDAV

# 3. 로그 관리
from patch.log import remote_registry

# 5. 보안 관리
from patch.security import force_exit


# 확인 코드
def main():
    # W-01 : 1. 계정관리 > 1.1 Administrator 계정 이름 변경 또는 보안성 강화
    print("Rename Result:", change_adminName.rename_administrator())

    if change_adminName.check_exist():
        print("Account name successfully changed")
    else:
        print("Account name change failed")

    # W-48 : 1. 계정관리 > 1.9 패스워드 복잡성 설정
    if pw_complexity.change_pwcomplexity():
        print("PasswordComplexity changed to 1")

    if pw_complexity.check_pwcomplexity():
        print("Password complexity is enabled.")
    else:
        print("The password complexity is disabled or cannot be determined.")

    # W-49 : 1. 계정관리 > 1.10 패스워드 최소 암호 길이
    result = subprocess.run(["powershell", "-Command", "net accounts"], capture_output=True, text=True)
    output = result.stdout
    match = re.search(r"Minimum password length:\s+(\d+)", output)

    changed = pw_length.check_pwlen()

    print("Command Execution Output:", pw_length.change_pwlen())
    print("Minimum Password Length Changed:", changed)
    print("Password Policy Check Output:", match.group(0))

    # W-50 : 1. 계정관리 > 1.11 패스워드 최대 사용 기간
    result = subprocess.run(["powershell", "-Command", "net accounts"], capture_output=True, text=True)
    output = result.stdout
    match = re.search(r"Maximum password age \(days\):\s+(\d+)", output)

    changed = pw_maxperiod.check_maxperiod()

    print("Command Execution Output:", pw_maxperiod.change_maxperiod())
    print("Maximum password age Changed:", changed)
    print("Password Policy Check Output:", match.group(0))

    # W-16 : 2. 서비스관리 > 2.10 IIS 링크 사용 금지
    disable_link.disable_directory_browsing()

    # W-17 : 2. 서비스관리 > 2.11 IIS 파일 업로드 및 다운로드 제한
    limit_bytes = 1048576 # 업로드 및 다운로드 크기 제한을 1MB로 설정
    print(f"Current upload and download limit: {current_limit} bytes")
    limit_upload_download.set_limit(limit_bytes)

    # W-21 : 2. 서비스관리 > 2.15 IIS 미사용 스크립트 매핑 제거
    config_file_path = r'C:\Windows\System32\inetsrv\config\applicationHost.config'
    remove_mapping.remove_script_mappings(config_file_path)
    print("Script mappings removed successfully.")


    # W-23 : 2. 서비스관리 > 2.17 IIS WebDAV 비활성화
    config_path = r'C:\Windows\System32\inetsrv\config\applicationHost.config'
    disable_WebDAV.disable_webdav(config_path)

    # W-35 : 4. 로그관리 > 4.2 Remote Registry Control
    remote_registry.disable_remote_registry()

    # W-40 : 5.보안 관리 > 5.5 원격 시스템에서 강제로 시스템 종료
    if force_exit.remote_shutdown():
        print("remote shutdown privilege changed")

    if force_exit.check_Privilege():
        print("Now, Only the Administrator group has remote shutdown privilege.")
    else:
        print("The remote shutdown is not set correctly or cannot be determined.")
