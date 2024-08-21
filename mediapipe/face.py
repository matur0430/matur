import cv2
import mediapipe as mp

# MediaPipe Face Mesh 초기화
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 얼굴 표정을 인식하는 함수
def get_expression(landmarks):
    # 간단히 입의 열린 정도로 웃음과 무표정을 구분합니다.
    mouth_top = landmarks[13].y
    mouth_bottom = landmarks[14].y
    mouth_height = mouth_bottom - mouth_top
    
    left_eye_top = landmarks[159].y
    left_eye_bottom = landmarks[145].y
    left_eye_height = left_eye_bottom - left_eye_top
    
    right_eye_top = landmarks[386].y
    right_eye_bottom = landmarks[374].y
    right_eye_height = right_eye_bottom - right_eye_top

    if left_eye_height < 0.01 and right_eye_height < 0.01:
        return "Sleeping"
    elif mouth_height > 0.05:
        return "Smiling"
    elif mouth_height < 0.02:
        return "Angry"
    else:
        return "Neutral"

# 웹캠에서 비디오 스트림 읽기 및 얼굴 표정 인식 실행
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # BGR 이미지를 RGB로 변환
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 이미지 분석 및 결과 처리
    results = face_mesh.process(rgb_frame)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # 얼굴 표정 인식
            expression = get_expression(face_landmarks.landmark)
            cv2.putText(frame, expression, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2, cv2.LINE_AA)
            
            # 얼굴 특징점 그리기
            mp.solutions.drawing_utils.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,  # 얼굴 윤곽선 연결 사용
                landmark_drawing_spec=None,
                connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style())

    # 결과 화면 표시
    cv2.imshow('Face Expression Recognition', frame)
    
    if cv2.waitKey(5) & 0xFF == 27:  # ESC 키를 눌러 종료
        break

cap.release()
cv2.destroyAllWindows()
