import cv2

# 加载图片
img = cv2.imread('2.jpg')

# 将图片转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)

# 对灰度图像进行阈值处理，将灯的轮廓分离出来
ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# 计算灯的亮度
brightness = float(cv2.countNonZero(thresh) / (img.shape[0] * img.shape[1]))

# 输出灯的亮度
if brightness > 0.5:
    print("灯是亮着的")
else:
    print("灯是灭的")

