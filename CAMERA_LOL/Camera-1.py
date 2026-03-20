from pynput import keyboard
import cv2
cap = cv2.VideoCapture(0)
def on_press(key):
    try:
        if key == keyboard.Key.esc:
            return False
        elif key == keyboard.Key.space:
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Captured Image', frame)
                cv2.waitKey(1)  
    except Exception as e:
        print(e)
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
cap.release()
cv2.destroyAllWindows()