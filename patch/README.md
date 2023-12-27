## 패치 기능 구현 
### 1. 계정관리 : account
|파일명|항목코드|항목|테스트여부|
|:------:|:------:|:---:|:---:|
|`change_adminName.py`|W-01|Administrator 계정 이름 변경|O|
|`pw_complexity.py`|W-48|패스워드 복잡성 설정|X|
|`pw_length.py`|W-49|패스워드 최소 암호 길이|O|
|`pw_maxperiod.py`|W-50|패스워드 최대 사용 기간|O|

### 2. 서비스 관리 : service
|파일명|항목코드|항목|테스트여부|
|:------:|:------:|:---:|:---:|
|`disable_link.py`|W-16|IIS 링크 사용 금지|O|
|`limit_upload_download.py`|W-16|IIS 링크 사용 금지|O|
|`remove_mapping.py`|W-21|IIS 미사용 스크립트 매핑 제거|X|
|`disable_WebDAV.py`|W-23|IIS WebDAV 비활성화|X|

### 4. 로그 관리 : log
|파일명|항목코드|항목|테스트여부|
|:------:|:------:|:---:|:---:|
|`remote_registry.py`|W-35|Remote Registry Control|X|

### 5. 보안 관리 : security
|파일명|항목코드|항목|테스트여부|
|:------:|:------:|:---:|:---:|
|`administrator.py`|W-40|원격 시스템에서 강제로 시스템 종료|X|
