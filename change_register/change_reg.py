import winreg as reg

try:
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies", 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(key, "ActiveDesktop", 0, reg.REG_DWORD, 0)
    print(reg.QueryValueEx(key, "ActiveDesktop"))
    reg.CloseKey(key)
except Exception as e:
    print(f"Error: {e}")