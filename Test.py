import cv2

# # 人脸检测器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascades_frontalface_default.xml')
# 眼睛检测器
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascades_eye.xml')
# 嘴巴检测器
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascades_mcs_mouth.xml')
# 鼻子检测器
nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascades_mcs_nose.xml')

# 获取摄像头
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 打开摄像头
cap.open(0)
cv2.namedWindow('mytest', 0)
cv2.resizeWindow('mytest', 1500, 1000)
while cap.isOpened():
    # 获取画面
    flag, frame = cap.read()

    # 人脸识别
    faces = face_cascade.detectMultiScale(frame, 1.3, 2)
    img = frame
    for (x, y, w, h) in faces:
        # 根据人脸坐标和长度，宽度画出矩形
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 确定人脸范围，在人脸上搜索其他特征
        face_area = img[y:y + h, x:x + w]
        # 人眼检测
        eyes = eye_cascade.detectMultiScale(face_area, 1.3, 2)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 1)
        # 嘴巴检测
        mouth = mouth_cascade.detectMultiScale(face_area, 1.5, 2)
        for (mx, my, mw, mh) in mouth:
            cv2.rectangle(face_area, (mx, my), (mx + mw, my + mh), (0, 0, 255), 2)
        # 鼻子检测
        nose = nose_cascade.detectMultiScale(face_area, 1.3, 2)
        for (nx, ny, nw, nh) in nose:
            cv2.rectangle(face_area, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 1)

    # 画面显示
    cv2.imshow('mytest', img)
    # 设置退出按钮
    key_pressed = cv2.waitKey(100)
    print('单机窗口,输入按键，电脑按键为', key_pressed, '按esc键结束')
    if key_pressed == 27:
        break
# 关闭摄像头
cap.release()
# 关闭图形窗口
cv2.destroyAllWindows()
