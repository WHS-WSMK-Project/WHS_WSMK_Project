import tkinter as tk

# 윈도우의 크기를 설정하는 상수
window_width = 600
window_height = 400

# 버튼 클릭 이벤트를 처리하는 함수
def on_button_click(button_text):
    print(f"{button_text} 버튼이 클릭되었습니다.")

# 메인 윈도우 생성
root = tk.Tk()
root.title("보안 패치 관리자")
root.geometry(f"{window_width}x{window_height}")  # 윈도우 크기 지정

# 맨 위의 텍스트 라벨 생성 및 배치
header_label = tk.Label(root, text="다음과 같은 항목을 패치합니다. 세부사항은 각 항목을 클릭하세요.", font=("Arial", 10))
header_label.grid(row=0, column=0, columnspan=2, pady=10)

# 카테고리별 프레임 생성 및 배치
account_frame = tk.LabelFrame(root, text="계정관리")
service_frame = tk.LabelFrame(root, text="서비스관리")
log_frame = tk.LabelFrame(root, text="로그관리")
security_frame = tk.LabelFrame(root, text="보안 관리")

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
        button = tk.Button(frame, text=item, command=lambda text=item: on_button_click(text))
        button.grid(row=row_count, column=0, sticky="ew", padx=5, pady=2)
        row_count += 1

# Go, Back 버튼 생성 및 배치
bottom_frame = tk.Frame(root)
bottom_frame.grid(row=3, column=0, columnspan=2, pady=10)

go_button = tk.Button(bottom_frame, text="Patch", command=lambda: on_button_click("Go"))
go_button.pack(side=tk.RIGHT)

back_button = tk.Button(bottom_frame, text="Back", command=lambda: on_button_click("Back"))
back_button.pack(side=tk.RIGHT, padx=10)

# 루트 윈도우의 grid 설정
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# 메인 루프 시작
root.mainloop()
