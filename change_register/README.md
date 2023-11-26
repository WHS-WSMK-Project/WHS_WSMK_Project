## 레지스터 변경 실습 코드 
모든 레지스터 실습은 `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\ActiveDesktop\NoChangingWallPaper` 
경로에 존재하는 **바탕 화면 배경 변경 금지** 설정 변경 실습

### change_reg.py
- `python`에서 `winreg` 모듈을 통한 레지스트리 변경

### chreg_powershell.py
- `python`에서 `subprocess` 모듈로 powershell 명령을 내려 변경
  
### change_reg.ps1
- powershell 명령을 `.ps1` 스크립트로 만들어 변경
