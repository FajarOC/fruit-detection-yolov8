# 🍎 YOLOv8 Fruit Detection dengan Streamlit

Deteksi buah otomatis menggunakan YOLOv8 yang dibungkus dalam aplikasi Streamlit, memudahkan kamu melakukan deteksi buah melalui web secara real-time.

---

## 🚀 Fitur
✅ Menggunakan YOLOv8 untuk mendeteksi buah dari gambar yang diupload  
✅ Antarmuka **Streamlit Web App** yang mudah digunakan  
✅ Visualisasi **hasil deteksi vs gambar asli** secara berdampingan  
✅ **Deployable ke Docker** dan dapat dijalankan di lokal atau server

---

## 📂 Struktur Proyek
fruit-detection-yolov8/
│
├── .ipynb_checkpoints/       # (Otomatis Jupyter, dapat diabaikan)
├── datasets/                 # Dataset buah untuk training (optional, sebaiknya besar tidak di-push)
├── images/                   # Gambar untuk uji coba dan hasil deteksi
├── runs/detect/              # Hasil deteksi YOLOv8 (optional)
│
├── .gitignore                # File untuk mengabaikan file tertentu saat push
├── app.py                    # Streamlit app utama untuk deteksi buah
├── dockerfile                # File Docker untuk containerisasi aplikasi
├── fruit_detection_model.pt  # Model YOLOv8 hasil training
├── fruits.ipynb              # Notebook untuk training/eksperimen YOLOv8
├── requirements.txt          # Dependensi utama
└── yolov8n.pt                # Pre-trained YOLOv8n (optional untuk transfer learning)

🚀 Fitur
✅ Deteksi buah (jeruk, apel, pisang, dll) dengan YOLOv8.
✅ Visualisasi bounding box, confidence score, dan label.
✅ Aksesible via web dengan Streamlit.
✅ Siap dijalankan lokal atau di dalam Docker container.
✅ Cocok untuk belajar pipeline Computer Vision YOLOv8.

⚙️ Cara Menjalankan
1️⃣ Jalankan Lokal
    pip install -r requirements.txt
    streamlit run app.py
Buka browser di:
http://localhost:8501

2️⃣ Jalankan dengan Docker
Build Image:
    docker build -t fruit-app .
Run Container:
    docker run -p 8501:8501 fruit-app
Buka browser di:
    http://localhost:8501

🏗️ Training YOLOv8
Dataset dapat diletakkan di folder datasets/.

Gunakan fruits.ipynb untuk melakukan training YOLOv8.

Model hasil training dapat disimpan sebagai fruit_detection_model.pt untuk digunakan pada aplikasi Streamlit.

🛠️ Dependensi Utama
Python 3.10

torch

torchvision

ultralytics

opencv-python

streamlit

matplotlib

pillow

☁️ Deployment
Repo ini siap untuk:
✅ Local Deployment
✅ Docker Deployment
✅ Siap untuk di-deploy ke AWS/GCP/Azure/Vercel/Streamlit Community Cloud sesuai kebutuhan.

📜 Lisensi
Proyek ini bersifat edukasi, bebas digunakan untuk pembelajaran dan pengembangan lebih lanjut.

