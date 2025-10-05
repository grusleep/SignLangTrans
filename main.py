import cv2
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer, Qt

class SignLanguageTranslator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("수어 번역기")
        self.setGeometry(100, 100, 800, 600)

        # 중앙 위젯 및 레이아웃 설정
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 카메라 영상을 표시할 라벨
        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.video_label)

        # 번역된 텍스트를 표시할 라벨
        self.text_label = QLabel("번역된 텍스트가 여기에 표시됩니다.", self)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.text_label)

        # 레이아웃 비율 설정 (영상:텍스트 = 4:1)
        self.layout.setStretch(0, 4)
        self.layout.setStretch(1, 1)

        # 카메라 설정
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.text_label.setText("카메라를 열 수 없습니다.")
            return

        # QTimer를 사용하여 주기적으로 프레임 업데이트
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 30ms 마다 업데이트 (약 33fps)

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.text_label.setText("프레임을 수신할 수 없습니다.")
            self.timer.stop()
            return

        # OpenCV 프레임(BGR)을 PyQt가 사용할 수 있는 QImage(RGB)로 변환
        frame = cv2.flip(frame, 1) # 좌우 반전
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)

        # QImage를 QPixmap으로 변환하여 라벨에 표시
        pixmap = QPixmap.fromImage(qt_image)
        # video_label의 크기에 맞게 이미지 스케일 조정
        scaled_pixmap = pixmap.scaled(self.video_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.video_label.setPixmap(scaled_pixmap)

    def closeEvent(self, event):
        # 애플리케이션 종료 시 카메라 자원 해제
        self.cap.release()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignLanguageTranslator()
    window.show()
    sys.exit(app.exec())