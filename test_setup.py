# test_setup.py
# Run this to check everything installed correctly

print("=" * 50)
print("  AI CARPOOL COMPLIANCE - SETUP VERIFICATION")
print("=" * 50)

all_good = True

# Test OpenCV
try:
    import cv2
    print(f"✅ OpenCV       : {cv2.__version__}")
except ImportError:
    print("❌ OpenCV       : FAILED - run: pip install opencv-python")
    all_good = False

# Test PyTorch
try:
    import torch
    gpu = "✅ GPU Ready" if torch.cuda.is_available() else "⚠️  CPU Only (No GPU)"
    print(f"✅ PyTorch      : {torch.__version__} | {gpu}")
except ImportError:
    print("❌ PyTorch      : FAILED - run: pip install torch")
    all_good = False

# Test YOLOv8
try:
    from ultralytics import YOLO
    print(f"✅ YOLOv8       : Ready")
except ImportError:
    print("❌ YOLOv8       : FAILED - run: pip install ultralytics")
    all_good = False

# Test DeepSORT
try:
    from deep_sort_realtime.deepsort_tracker import DeepSort
    print(f"✅ DeepSORT     : Ready")
except ImportError:
    print("❌ DeepSORT     : FAILED - run: pip install deep-sort-realtime")
    all_good = False

# Test MediaPipe
try:
    import mediapipe as mp
    print(f"✅ MediaPipe    : {mp.__version__}")
except ImportError:
    print("❌ MediaPipe    : FAILED - run: pip install mediapipe")
    all_good = False

# Test EasyOCR
try:
    import easyocr
    print(f"✅ EasyOCR      : Ready")
except ImportError:
    print("❌ EasyOCR      : FAILED - run: pip install easyocr")
    all_good = False

# Test FastAPI
try:
    import fastapi
    print(f"✅ FastAPI      : {fastapi.__version__}")
except ImportError:
    print("❌ FastAPI      : FAILED - run: pip install fastapi")
    all_good = False

# Test SQLAlchemy
try:
    import sqlalchemy
    print(f"✅ SQLAlchemy   : {sqlalchemy.__version__}")
except ImportError:
    print("❌ SQLAlchemy   : FAILED - run: pip install sqlalchemy")
    all_good = False

# Test NumPy
try:
    import numpy as np
    print(f"✅ NumPy        : {np.__version__}")
except ImportError:
    print("❌ NumPy        : FAILED - run: pip install numpy")
    all_good = False

print("=" * 50)
if all_good:
    print("🎉 ALL GOOD! You are ready to build!")
else:
    print("⚠️  Some packages failed. Fix them above.")
print("=" * 50)