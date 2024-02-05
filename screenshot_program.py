import pyautogui
import tkinter as tk
from PIL import Image, ImageEnhance
import pytesseract
import os

def screenshot():

    # 鼠标左键点击->显示子窗口 
    def button_1(event):
        global x, y ,xstart,ystart
        x, y = event.x, event.y
        xstart,ystart = event.x, event.y
        # print("event.x, event.y = ", event.x, event.y)
        xstart,ystart = event.x, event.y  
        rectangle_frame.configure(height=1)
        rectangle_frame.configure(width=1)           
        rectangle_frame.place(x=event.x, y=event.y)

    # 鼠标左键移动->改变子窗口大小
    def b1_Motion(event):
        global x, y,xstart,ystart
        x, y = event.x, event.y
        # print("event.x, event.y = ", event.x, event.y)
        rectangle_frame.configure(height = event.y - ystart)
        rectangle_frame.configure(width = event.x - xstart)

    # 鼠标左键释放->记录最后光标的位置
    def buttonRelease_1(event):
        global xend,yend
        xend, yend = event.x, event.y

    #鼠标右键点击->截屏并保存图片
    def button_3(event):
        global xstart,ystart,xend,yend
        # cv.place_forget()
        rectangle_frame.place_forget()
        img = pyautogui.screenshot(region=[xstart,ystart,xend-xstart,yend-ystart]) # x,y,w,h
        img.save('screenshot.png')
        sys_out(None)

    def sys_out(even):
        scroot.destroy()
            
    scroot = tk.Tk()
    # 隐藏窗口的标题栏
    scroot.overrideredirect(True)
    #给屏幕变黑
    scroot.attributes("-alpha", 0.1)  
    scroot.geometry("{0}x{1}+0+0".format(scroot.winfo_screenwidth(), scroot.winfo_screenheight()))
    scroot.configure(bg="black")
    scroot.attributes('-topmost', 1) 
    
    # 创建Frame，表示方框
    rectangle_frame = tk.Frame(scroot, width=0, height=0, bg="blue")

    #坐标
    x, y = 0, 0
    xstart,ystart = 0 ,0
    xend,yend = 0, 0
    # rec = ''

    # canvas = tk.Canvas(scroot)
    # #提示小标签
    # canvas.configure(width=52)
    # canvas.configure(height=20)
    # canvas.configure(bg="yellow")
    # canvas.configure(highlightthickness=0)  # 高亮厚度
    # canvas.place(x=(scroot.winfo_screenwidth()-52),y=(0))
    # canvas.create_text(26, 12,font='Arial -12 bold',text='右键识别')

    # 绑定事件
    scroot.bind("<Button-1>", button_1)  # 鼠标左键点击->显示子窗口 
    scroot.bind("<B1-Motion>", b1_Motion)# 鼠标左键移动->改变子窗口大小
    scroot.bind("<ButtonRelease-1>", buttonRelease_1) # 鼠标左键释放->记录最后光标的位置
    scroot.bind("<Button-3>",button_3)   #鼠标右键点击->截屏并保存图片
    scroot.mainloop()

#对图像进行ocr  
def ocr_image(image_path,language,willenhance="None"):
    image = Image.open(image_path)
    if willenhance == "Thresholding":
        thresholding_result(image,willenhance)
        eimage = Image.open("screenshotConverted.jpg")
        text = pytesseract.image_to_string(eimage,lang=str(language))
    elif willenhance == "BW":
        text = pytesseract.image_to_string(image.convert('L'),lang=str(language))
    elif willenhance == "BWEnhance":
        image = image.convert('L')
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(1.5)
        enhanced_image.save("screenshot.png")
        text = pytesseract.image_to_string(enhanced_image,lang=str(language))
    else:
        text = pytesseract.image_to_string(image,lang=str(language))
    return text

#截图并ocr
def shot_and_ocr():
    screenshot()
    return ocr_image("screenshot.png","jpn+equ", "BWEnhance") #可以在参数那里更改语言


#设置阈值
def thresholding_result(image_object,option):
    if option:
        Img = image_object.convert('L')
        threshold = 70       
        table = []  
        for i in range(256):
            if i < threshold:
                table.append(1)
            else:
                table.append(0)
        photo = Img.point(table, '1')
        photo.save("screenshotConverted.jpg")
    else:
        pass
