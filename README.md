# 🚗 AI Carpool Compliance System

## Project Overview
An AI-powered system that analyzes traffic camera footage 
to detect carpool lane violations.

## Features
- Vehicle Detection using YOLOv8
- Vehicle Tracking using DeepSORT  
- Occupant Counting using MediaPipe
- Number Plate Recognition using OCR
- Violation Tracking and Challan Generation
- Analytics Dashboard

## Tech Stack
- Python 3.10+
- OpenCV, YOLOv8, DeepSORT
- MediaPipe, EasyOCR
- FastAPI, SQLAlchemy
- Docker

## Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python test_setup.py