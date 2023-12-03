import winreg

def print_reg_values(hkey, key):
    try:
        reg_key = winreg.OpenKey(hkey, key, 0, winreg.KEY_READ)

        for i in range(winreg.QueryInfoKey(reg_key)[1]):
            name, value, _ = winreg.EnumValue(reg_key, i)
            print("{}\\{}: {} = {}".format(key, name, value, _))

        winreg.CloseKey(reg_key)
    except Exception as e:
        print("Error accessing key {}: {}".format(key, e))

def print_all_reg(hkeys):
    for hkey in hkeys:
        try:
            print("==== {} ====".format(hkey))
            print_reg_keys(hkey, "")
            print("\n")
        except Exception as e:
            print("Error accessing HKEY {}: {}".format(hkey, e))

def print_reg_keys(hkey, key, indent=0):
    try:
        subkey = winreg.OpenKey(hkey, key, 0, winreg.KEY_READ)
        
        for i in range(winreg.QueryInfoKey(subkey)[0]):
            subkey_name = winreg.EnumKey(subkey, i)
            print("  " * indent + subkey_name)
            print_reg_keys(hkey, key + "\\" + subkey_name, indent + 1)
            print_reg_values(hkey, key + "\\" + subkey_name)
        
        winreg.CloseKey(subkey)
    except Exception as e:
        print("Error accessing key {}: {}".format(key, e))

hkeys = [winreg.HKEY_CLASSES_ROOT, winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_USERS, winreg.HKEY_CURRENT_CONFIG]

print_all_reg(hkeys)
