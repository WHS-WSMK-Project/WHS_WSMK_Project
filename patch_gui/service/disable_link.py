# W-16 : 2. 서비스관리 > 2.10 IIS 링크 사용 금지

import os

def remove_lnk_files(directory):
    # 디렉터리 내의 모든 파일 목록 가져오기
    files = os.listdir(directory)

    # .lnk 확장자를 가진 파일 삭제
    for file in files:
        if file.endswith(".lnk"):
            file_path = os.path.join(directory, file)
            os.remove(file_path)

    # 변경된 내용이 없을 경우 메시지 출력
    if not any(file.endswith(".lnk") for file in files):
        return False
    
    return True
