# W-23 : 2. 서비스관리 > 2.17 IIS WebDAV 비활성화

import xml.etree.ElementTree as ET
import os

def disable_webdav(filepath=r'C:\Windows\System32\inetsrv\config\applicationHost.config'):
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()

        isapi_cgi_restriction = root.find(".//isapiCgiRestriction")

        if isapi_cgi_restriction is not None:
            webdav_add_element = isapi_cgi_restriction.find('.//add[@path="%windir%\\system32\\inetsrv\\webdav.dll"]')

            if webdav_add_element is not None:
                webdav_add_element.set('allowed', 'false')
                tree.write(filepath)
                return True
            else:
                return False
        else:
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
