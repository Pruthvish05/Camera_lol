import cv2
import face_recognition 
cp = cv2.VideoCapture(0)
if not cp.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cp.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(frame,f"faces: {len(face_locations)}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cp.release()
cv2.destroyAllWindows()

