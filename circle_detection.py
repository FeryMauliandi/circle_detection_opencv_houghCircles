import cv2
import numpy as np

cap = cv2.VideoCapture(1)
font = cv2.FONT_HERSHEY_SIMPLEX

def draw_center_point(frame):
    height, width, _ = frame.shape
    center_x = int(width / 2)
    center_y = int(height / 2)
    cv2.circle(frame, (center_x, center_y), 5, (255, 0, 255), -1)
    return center_x, center_y


def detect_circles(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, minDist=100,
                              param1=50, param2=30, minRadius=50, maxRadius=150)
    
    center_x, center_y = draw_center_point(frame)
    Lingkaran = False
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        Lingkaran = True
        
        for (x, y, r) in circles:
            tolerance = 20 
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv2.circle(frame, (x, y), tolerance, (255, 0, 0), 2)
            cv2.line(frame, (center_x, center_y), (x, y), (0, 255, 255), 2)
            break

    
    cv2.putText(frame, "lingkaran terdeteksi = " + str(Lingkaran), (5, 20), font, 0.8, (0 , 255, 0), 2, cv2.LINE_AA)
    return frame


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    frame = detect_circles(frame)
    
    cv2.imshow("circle detection", frame)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()