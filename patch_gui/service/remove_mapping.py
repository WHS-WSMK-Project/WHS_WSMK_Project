# W-21 : 2. 서비스관리 > 2.15 IIS 미사용 스크립트 매핑 제거


import re

def remove_script_mappings(config_path):
    try:
        with open(config_path, 'r') as file:
            config_content = file.read()

        pattern = r'<add name="[^"]+" path="(\.(htr|idc|stm|shtm|shtml|printer|htw|ida|idq))" .* />'
        matches = re.finditer(pattern, config_content, re.IGNORECASE)


        changes_made = False

        for match in matches:
            path_to_remove = match.group(1)
            config_content = config_content.replace(match.group(0), '') 
            changes_made = True

        if not changes_made:
            return False

        with open(config_path, 'w') as file:
            file.write(config_content)
        
        return True

    except FileNotFoundError:
        print(f"Error: File not found - {config_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
