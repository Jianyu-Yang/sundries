import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract
import pandas as pd


def imageTonum(image,i,j,frames_num):
    # time_start = time.time()
    #cv.imwrite(r"C:\Users\Administrator\Desktop\photos\{}.png".format(str(i)),image1)
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 7')  # 使用简体中文解析图片
    try:
        text=float(text)
    except:
        print("发生异常:%s"%text)
        cv.namedWindow('input_image', cv.WINDOW_NORMAL)  # 设置为WINDOW_NORMAL可以任意缩放
        cv.imshow('input_image', image)
        # k = cv.waitKey(0)  # waitkey代表读取键盘的输入，括号里的数字代表等待多长时间，单位ms。 0代表一直等待
        # if k == 27:  # 键盘上Esc键的键值
        #     cv.destroyAllWindows()
        cv.waitKey(0)
        cv.destroyAllWindows()
        text=float(input('正确的数字是：'))   # todo 类型转换：float
        numarray[i][j]=text
        # cv.destroyAllWindows()
        print("%i/%i:input num=%f"%((i+1),frames_num,text))
    else:
        numarray[i][j] = text
        print("%i/%i:OCR num=%f"%((i+1),frames_num,text))
    # cv.imshow("ROI", image)

cap = cv.VideoCapture(r"C:\Users\Administrator\Desktop\PTW-BeamAdjust-Video\330-DR-5X5.mp4") # 调整参数实现读取视频或调用摄像头
frames_num=int(cap.get(7))
print("该视频总帧数为：%i"%frames_num)
numarray = np.zeros((frames_num,4))
i=0
while 1:
    ret, frame = cap.read()
    image1 = frame[224:251, 175:240]
    image2 = frame[258:283, 175:240]
    image3 = frame[224:251,1127:1192]
    image4 = frame[258:283,1127:1192]
    # cv.imwrite(r"C:\Users\Administrator\Desktop\test-photos\1.png", image1)
    # cv.imwrite(r"C:\Users\Administrator\Desktop\test-photos\2.png", image2)
    # cv.imwrite(r"C:\Users\Administrator\Desktop\test-photos\3.png", image3)
    # cv.imwrite(r"C:\Users\Administrator\Desktop\test-photos\4.png", image4)

    imageTonum(image1, i, 0, frames_num)
    imageTonum(image2, i, 1, frames_num)
    imageTonum(image3, i, 2, frames_num)
    imageTonum(image4, i, 3, frames_num)
    i=i+1
    if i==frames_num:
        df = pd.DataFrame(numarray)
        writer = pd.ExcelWriter('measure_data.xlsx')
        df.to_excel(writer, 'page_1', float_format='%.5f')
        #df.to_excel("meature_data.xlsx", index=False)
        writer.save()
        break
    # if cv.waitKey(50) & 0xff == ord('q'):
    #     break

print("已完成！")