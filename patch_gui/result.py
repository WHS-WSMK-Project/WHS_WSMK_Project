import tkinter as tk

class ThirdWindowScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        header_label = tk.Label(self, text="다음과 같은 항목이 패치 되었습니다.", font=("Arial", 10))
        header_label.grid(row=0, column=0, columnspan=2, pady=10)

        # 카테고리별 프레임 생성 및 배치
        account_frame = tk.LabelFrame(self, text="계정관리")
        service_frame = tk.LabelFrame(self, text="서비스관리")
        log_frame = tk.LabelFrame(self, text="로그관리")
        security_frame = tk.LabelFrame(self, text="보안 관리")

        account_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        service_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        log_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        security_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # 각 프레임에 버튼 추가
        buttons = {
            "계정관리": [
                "Administrator 계정 이름 변경 또는 보안성 강화",
                "패스워드 복잡성 설정",
                "패스워드 최소 암호 길이 설정",
                "패스워드 최대 사용 기간 설정"
            ],
            "서비스관리": [
                "IIS 링크 사용 금지",
                "IIS 파일 업로드 및 다운로드 제한",
                "IIS 미사용 스크립트 매핑 제거",
                "IIS WebDAV 비활성화"
            ],
            "로그관리": ["Remote Registry Control 사용안함"],
            "보안 관리": ["원격 시스템에서 강제로 시스템 종료 방지"]
        }

        frames = {
            "계정관리": account_frame,
            "서비스관리": service_frame,
            "로그관리": log_frame,
            "보안 관리": security_frame
        }

        # 버튼 색상 변경 로직
        for category, frame in frames.items():
            row_count = 0
            for item in buttons[category]:
                condition = True  
                button_color = "#2F9D27" if condition else "#FF2424"
                button = tk.Button(frame, text=item, bg=button_color)
                button.grid(row=row_count, column=0, sticky="ew", padx=5, pady=2)
                row_count += 1

        # 하단에 Close 버튼 추가
        bottom_frame = tk.Frame(self)
        bottom_frame.grid(row=3, column=0, columnspan=2, pady=10)

        close_button = tk.Button(bottom_frame, text="Close", command=self.close_window)
        close_button.pack(side=tk.RIGHT)

    def close_window(self):
        self.master.destroy()

# Tkinter 애플리케이션 시작
root = tk.Tk()
root.title("Third Window Screen")

# ThirdWindowScreen 인스턴스 생성 및 배치
third_window_screen = ThirdWindowScreen(root)
third_window_screen.pack(expand=True, fill='both')

# 메인 루프 실행
root.mainloop()
