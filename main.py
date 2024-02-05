import keyboard
import screenshot_program as scsp
import tkinter as tk
import threading
import sys
import text_process_program as txtpp
import hftranslate as hftrans
import solve_program as solp
import azuretranslate as aztrans

proc_mode = "j2z"

def shot_ocr_and_change_text():
    text = scsp.shot_and_ocr()
    #这里插入文字处理   
    text = txtpp.del_ugly_newlines(text)
    print(text)
    #根据模式进行选择，默认日文翻译中文
    if proc_mode == "j2z":
        # print(proc_mode)
        # text = hftrans.hf_translate(text,"jp")
        text = aztrans.aztranslate(text,"jp")
    elif proc_mode == "simplecal":
        # print(proc_mode)
        text = text+"\n"+ str(solp.proc_and_solve(text))
    elif proc_mode == "e2z":
        # print(proc_mode)
        # text = hftrans.hf_translate(text,"en")
        text = aztrans.aztranslate(text,"en")
    print(text)
    refresh_text(text)

#刷新显示的文字
def refresh_text(text_to_display):
    label.config(text=text_to_display,anchor='nw')

#开启键盘监听
def start_listener():
    def on_alt_a_pressed():
        print("Alt + A pressed!")
        threading.Thread(target=shot_ocr_and_change_text).start()
    def on_shift_esc_pressed():
        print("Tab + Esc pressed!")
        exitfunc()
        print('exited')
    # 监听器, 可以在这里设置快捷键
    keyboard.add_hotkey('alt+a', on_alt_a_pressed) #截图
    keyboard.add_hotkey('tab+esc', on_shift_esc_pressed) #退出

#退出并清除所有线程
def exitfunc():
    root.geometry(str(root.winfo_screenwidth())+'x'+str(root.winfo_screenheight())) 
    root.quit()
    sys.exit()

#################
#  GUI 操作部分  #
#################

def change_modelabel_text(new_text):
    modelabel.config(text=new_text)

def btnCalmode_click():
    change_modelabel_text("计算题模式")
    global proc_mode 
    proc_mode = "simplecal"

def btnJaToZhmode_click():
    change_modelabel_text("日文To中文模式")
    global proc_mode 
    proc_mode = "j2z"

def btnEnToZhmode_click():
    change_modelabel_text("英文To中文模式")
    global proc_mode 
    proc_mode = "e2z"

root = tk.Tk()
#隐藏标题栏
root.overrideredirect(True)
#设置置顶
root.attributes('-topmost', 1)
#设置背景颜色
root.configure(bg="black")
root.attributes('-alpha', 0.7)
#设置窗口大小
root.geometry("200x700")
#初始文字
label = tk.Label(root, text="Press Alt + A to trigger the action. Tab+Esc to quit",anchor='nw',justify="left",fg="blue", bg="yellow", wraplength=200)
label.pack()

#当前模式状态
modelabel = tk.Label(root, text="请选择模式,默认日译中",anchor='sw',font=("Helvetica", 10),justify="left",fg="red", bg="grey")
modelabel.pack(side=tk.BOTTOM,pady=10)

#更改模式按钮
# 创建一个 Frame 来放置按钮
button_frame = tk.Frame(root,background="black")
button_frame.pack(side=tk.BOTTOM, fill=tk.X)
# 创建计算题模式按钮
btnCalmode = tk.Button(button_frame, text="计算题", command=btnCalmode_click)
btnCalmode.pack(side=tk.LEFT,pady=5)
# 创建日文To中文按钮
btnJaToZhmode = tk.Button(button_frame, text="日译中", command=btnJaToZhmode_click)
btnJaToZhmode.pack(side=tk.LEFT,pady=5) 
# 创建英文To中文按钮
btnEnToZhmode = tk.Button(button_frame, text="英译中", command=btnEnToZhmode_click)
btnEnToZhmode.pack(side=tk.LEFT,pady=5)

# 在单独的线程中启动监听器
listener_thread = threading.Thread(target=start_listener)
listener_thread.start()

# 启动Tkinter主循环
root.mainloop()