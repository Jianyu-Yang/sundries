# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract
import pandas as pd

# 创建16:9矩形框，像素300dpi
plt.figure(figsize = (16,9), dpi = 300)
plt.subplot(111)

x = np.linspace(0, 40000, 40001, endpoint=True)
y = np.arccos(6371/(x+6371))
y = 12742 * y
plt.plot(x, y, color='blue', linewidth=2.0, linestyle='-')

# 设置X轴范围
plt.xlim(0,40000)
# 设置X轴标尺刻度，从-10到10，取21个值
plt.xticks(np.linspace(0,40000,41,endpoint=True))

# 设置y轴范围
plt.ylim(0,21000)
# 设置y轴标尺刻度，从-1到1，取5个值
plt.yticks(np.linspace(0,21000,22,endpoint=True))

df = pd.DataFrame(y)
writer = pd.ExcelWriter('measure_data.xlsx')
df.to_excel(writer, 'page_1', float_format='%.5f')
# df.to_excel("meature_data.xlsx", index=False)
writer.save()


plt.show()
