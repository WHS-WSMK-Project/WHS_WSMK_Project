import subprocess

# PowerShell 명령어
powershell_command = "ls Registry::HKCU\ -Recurse"

""" 모든 HKEY의 하위키 출력
powershell_command = (
    "ls Registry::HKCU\ -Recurse" +  # HKEY_CURRENT_USER
    "ls Registry::HKLM\ -Recurse;" + # HKEY_LOCAL_MACHINE
    "ls Registry::HKCR\ -Recurse;" + # HKEY_CLASSES_ROOT
    "ls Registry::HKU\ -Recurse;" + # HKEY_USERS
    "ls Registry::HKCC\ -Recurse" # HKEY_CURRENT_CONFIG
)
"""

# PowerShell 실행 및 결과 가져오기
result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

# 결과 출력 및 오류 출력
print("=== STDOUT ===")
print(result.stdout)

print("=== STDERR ===")
print(result.stderr)
