import xml.etree.ElementTree as ET

def remove_handler(xml_path, handler_name):
    # XML 파일 불러오기
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # 삭제할 핸들러 경로
    handler_path = f'.//handlers/add[@name="{handler_name}"]'

    # 핸들러 노드 찾기 및 삭제
    handler_nodes = root.findall(handler_path)
    if handler_nodes:
        for node in handler_nodes:
            parent_node = node.getparent()
            parent_node.remove(node)

        # 변경된 내용 저장
        tree.write(xml_path)
        print(f"Handler '{handler_name}' removed successfully")
    else:
        print(f"Cannot find handler '{handler_name}' to remove")

# 파일 경로와 제거할 핸들러 이름 설정
xml_file_path = 'C:\\Windows\\System32\\inetsrv\\config\\applicationHost.config'
handler_to_remove = 'ASPClassic'

# 핸들러 제거 함수 호출
remove_handler(xml_file_path, handler_to_remove)
