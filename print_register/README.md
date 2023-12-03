## 레지스터 출력 실습 코드 

### print_reg.py (실패)
- `winreg` 모듈을 통한 모든 레지스트리 출력 코드
- 일부 HKEY의 하위키가 출력되지 않는 문제 발생

### print_reg_ps.py
- `subprocess` 모듈을 통한 모든 레지스트리 출력코드
- powershell 명령을 통해 출력되도록 함
