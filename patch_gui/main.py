import tkinter as tk
from tkinter import PhotoImage

# 메인 윈도우 생성
root = tk.Tk()
root.title('WSMK Analytical Tools')

# 창 크기 및 위치 설정
window_width = 600
window_height = 400

# 스크린 중앙에 창 위치
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# 로고 이미지를 로드
logo_image = PhotoImage(file="logo.png")

# 로고를 배치할 레이블 위젯 생성 및 배치
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(pady=20)  # 위젯 사이의 여백 조정
# 레이블의 위치를 지정하여 배치
logo_x = 230
logo_y = 55

logo_label.place(x=logo_x, y=logo_y)

# 텍스트 레이블 생성 및 배치
text_label = tk.Label(root, text='WSMK Analytical Tools', font=('Arial', 22))
text_label.pack()
# 레이블의 크기와 위치를 지정하여 배치
label_x = 150 
label_y = 220 

text_label.place(x=label_x, y=label_y)

# 'Go' 버튼 생성 및 배치
go_button = tk.Button(root, text='Go', command=lambda: print("버튼이 클릭되었습니다."))
go_button.pack(pady=40)

# 버튼의 크기와 위치를 지정하여 배치
button_width = 100 
button_height = 40 
button_x = 450  
button_y = 310  

go_button.place(width=button_width, height=button_height, x=button_x, y=button_y)

# 창 실행
root.mainloop()