import re

def remove_script_mappings(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    pattern = re.compile(r'<handlers accessPolicy="Read, Script">.*?</handlers>', re.DOTALL)

    content = re.sub(pattern, '', content)

    with open(file_path, 'w') as file:
        file.write(content)

config_file_path = r'C:\Windows\System32\inetsrv\config\applicationHost.config'

remove_script_mappings(config_file_path)

print("Script mappings removed successfully.")
