import tkinter as tk
from tkinter import PhotoImage

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('WSMK Analytical Tools')
        self.set_window_center(600, 400)

        self.start_screen = StartScreen(self)
        self.option_screen = OptionScreen(self)

        self.show_start_screen()

    def set_window_center(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)
        self.geometry(f'{width}x{height}+{center_x}+{center_y}')

    def show_start_screen(self):
        self.option_screen.pack_forget()
        self.start_screen.pack()

    def show_option_screen(self):
        self.start_screen.pack_forget()
        self.option_screen.pack()

class StartScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        logo_image = PhotoImage(file="logo.png")
        logo_label = tk.Label(self, image=logo_image)
        logo_label.image = logo_image
        logo_label.pack(pady=20)

        text_label = tk.Label(self, text='WSMK Analytical Tools', font=('Arial', 22))
        text_label.pack()

        go_button = tk.Button(self, text='Go', command=master.show_option_screen)
        go_button.pack(pady=40)
        # go_button.place(width=100, height=40, x=115, y=250)

class OptionScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 맨 위의 텍스트 라벨 생성 및 배치
        header_label = tk.Label(self, text="다음과 같은 항목을 패치합니다. 세부사항은 각 항목을 클릭하세요.", font=("Arial", 10))
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

        # 각 프레임에 버튼을 추가하고 grid로 배치
        for category, frame in frames.items():
            row_count = 0
            for item in buttons[category]:
                button = tk.Button(frame, text=item)
                button.grid(row=row_count, column=0, sticky="ew", padx=5, pady=2)
                row_count += 1

        # Go, Back 버튼 생성 및 배치
        bottom_frame = tk.Frame(self)
        bottom_frame.grid(row=3, column=0, columnspan=2, pady=10)

        go_button = tk.Button(bottom_frame, text="Patch", command=master.show_start_screen)
        go_button.pack(side=tk.RIGHT)

        back_button = tk.Button(bottom_frame, text="Back", command=master.show_start_screen)
        back_button.pack(side=tk.RIGHT, padx=10)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
