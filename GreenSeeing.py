import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
#C=int(input("摄像头:(0为前置，1为来自USB)"))
#M=input("识别模式:T为实时，F为图片")
def colorTacing(cho,mod):
	#默认识别绿色
    color_lower = np.array([20, 20,0])
    color_upper = np.array([90, 255,255])
    cap = cv2.VideoCapture(cho)
    cap.set(3, 320)
    cap.set(4, 240)
    while mod=="T":
        ret, frame = cap.read()
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, color_lower, color_upper)
        # 图像学膨胀腐蚀
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.GaussianBlur(mask, (3, 3), 0)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        # 寻找轮廓并绘制轮廓
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        gpixel_count = (mask.reshape(-1, 1)[:, 0] != 0).sum()
        print("绿视率:"+str((gpixel_count/mask.size)*100)+"%")
        if cv2.waitKey(5) & 0xFF == 27:
            break
    if mod=="F":
        f=filedialog.askopenfilename()
        frame =cv2.imread(f)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, color_lower, color_upper)
            # 图像学膨胀腐蚀
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.GaussianBlur(mask, (3, 3), 0)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        gpixel_count = (mask.reshape(-1, 1)[:, 0] != 0).sum()
        print("绿视率:" + str((gpixel_count / mask.size) * 100) + "%")
        cv2.waitKey(5) & 0xFF == 27
        input()
        cap.release()
    cv2.destroyAllWindows()

##colorTacing(C,M)


window = Tk()
window.title("GreenSeeing")
var1 = IntVar()
var2 = StringVar()
r1 = Radiobutton(window, text='使用前置摄像头',variable=var1, value=0).pack()
r2 = Radiobutton(window, text='使用USB摄像头', variable=var1, value=1).pack()
r3 = Radiobutton(window, text='捕捉模式', variable=var2, value='T').pack()
r4 = Radiobutton(window, text='文件模式', variable=var2, value='F').pack()
def Get():print(colorTacing(var1.get(), var2.get()))
B=Button(window,text='开始',command=Get).pack()
window.mainloop()


