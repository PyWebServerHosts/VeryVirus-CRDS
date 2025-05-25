import ffmpeg
import pygame
import tempfile
import time
import os
import cv2

# Input video path
video_path = "kltr.mp4"

# OpenCV to "open" the video (optional, per your requirement)
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
  pass
    exit()

# Extract audio once to temp file using ffmpeg
with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
    audio_path = temp_audio.name

ffmpeg.input(video_path).output(audio_path, format='mp3', acodec='libmp3lame', vn=None).run(overwrite_output=True)

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load(audio_path)



try:
    while True:
        # Start playing audio from the beginning
        pygame.mixer.music.play()
        print("Looping audio...")        # Wait while audio is playing
        while pygame.mixer.music.get_busy():
            ret, _ = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            time.sleep(0.1)

except KeyboardInterrupt:
   pass

finally:
    pygame.mixer.music.stop()
    cap.release()
    os.remove(audio_path)
