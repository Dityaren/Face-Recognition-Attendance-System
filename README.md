# Face Recognition Attendance System

This is a simple attendance system using face recognition implemented in Python. The system allows users to mark attendance by capturing their face through a webcam.

## Installation

To run the program, follow these steps:

1. Install the required libraries:
```bash
pip install opencv-python
pip install numpy
pip install face-recognition
pip install Pillow
```

2. Download the code file `attendance_system.py` and save it to your local machine.

3. Run the program:
```bash
python attendance_system.py
```

## Usage

1. When the program starts, it will access the webcam to capture your face.

2. Click the "Absen Masuk" button to mark your attendance as "Masuk" (in) or "Absen Keluar" button to mark your attendance as "Keluar" (out).

3. The program will compare your face with the stored images in the `gambar` directory and recognize your identity.

4. If your face is recognized, the program will update the attendance record in the `Absensi.csv` file with your name and the current timestamp.

5. The webcam will display the live video feed with your face highlighted.

## Contributing

If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

**Note:** Ensure that you have a webcam connected to your machine to run the program successfully.
