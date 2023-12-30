## 패치 CLI ver 사용법
#### 1. github에 위치한 `patch` 폴더 다운로드
#### 2. patch 폴더를 `C:` 아래 위치시킬것 → `C:\patch`
#### 3. 해당 파일의 경로 :  `dist/MSWK.exe`

## 패치 기능 구현 
### 1. 계정관리 : account
|파일명|항목코드|항목|테스트여부|
|:------:|:------:|:---:|:---:|
|`change_adminName.py`|W-01|Administrator 계정 이름 변경|O|
|`pw_complexity.py`|W-48|패스워드 복잡성 설정|O|
|`pw_length.py`|W-49|패스워드 최소 암호 길이|O|
|`pw_maxperiod.py`|W-50|패스워드 최대 사용 기간|O|

### 2. 서비스 관리 : service
|파일명|항목코드|항목|테스트여부|
|:------:|:------:|:---:|:---:|
|`disable_link.py`|W-16|IIS 링크 사용 금지|O|
|`limit_upload_download.py`|W-17|IIS 파일 업로드 및 다운로드 제한|O|
|`remove_mapping.py`|W-21|IIS 미사용 스크립트 매핑 제거|O|
|`disable_WebDAV.py`|W-23|IIS WebDAV 비활성화|O|

### 4. 로그 관리 : log
|파일명|항목코드|항목|테스트여부|
|:------:|:------:|:---:|:---:|
|`remote_registry.py`|W-35|Remote Registry Control|O|

### 5. 보안 관리 : security
|파일명|항목코드|항목|테스트여부|
|:------:|:------:|:---:|:---:|
|`force_exit.py`|W-40|원격 시스템에서 강제로 시스템 종료|O|
