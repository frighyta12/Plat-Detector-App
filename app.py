from flask import Flask, request, jsonify
import numpy as np
import cv2
from detector import detect_license_plate
import traceback
import sys

app = Flask(__name__)

@app.route('/detect-plate', methods=['POST'])
def detect_plate():
    try:
        print("[INFO] Request POST diterima dari klien")

        if 'image' not in request.files:
            print("[ERROR] Tidak ada file 'image' dalam request")
            return jsonify({'results': []}), 400

        file = request.files['image']
        print(f"[INFO] File gambar diterima: {file.filename}")

        file_bytes = np.frombuffer(file.read(), np.uint8)
        print("[DEBUG] File dibaca ke numpy array")

        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        print("[DEBUG] Gambar didekode oleh OpenCV")

        if img is None:
            print("[ERROR] Gambar gagal didekode")
            return jsonify({'results': []}), 400

        print("[INFO] Memulai proses deteksi plat nomor...")
        plates = detect_license_plate(img)
        print(f"[DEBUG] Hasil dari fungsi deteksi: {plates}")

        return jsonify({'results': plates}) if plates else jsonify({'results': []})

    except Exception as e:
        print(f"[FATAL] Terjadi error di server: {str(e)}")
        traceback.print_exc(file=sys.stdout)
        return jsonify({'results': []}), 500
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
