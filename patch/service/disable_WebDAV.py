import xml.etree.ElementTree as ET

def disable_webdav(xml_path):
    # XML 파일 불러오기
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # WebDAV 룰의 경로
    webdav_path = ".//system.webServer/webdav/authoring/rules/rule"

    # WebDAV 룰 찾기
    webdav_rule = root.find(webdav_path)

    if webdav_rule is not None:
        # 'allowed' 속성 값을 "false"로 변경
        webdav_rule.set('allowed', 'false')
        # 변경된 내용 저장
        tree.write(xml_path)
        print("WebDAV is disabled.")
    else:
        print("WebDAV is not found..")

# 파일 경로 설정
xml_file_path = 'C:\\Windows\\System32\\inetsrv\\config\\applicationHost.config'

# 함수 호출
disable_webdav(xml_file_path)