import easyocr
import cv2
import traceback

reader = easyocr.Reader(['en'])

def detect_license_plate(img):
    try:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = reader.readtext(img_rgb)

        plates = []
        for bbox, text, prob in results:
            if len(text) >= 4:
                plates.append({
                    "text": text,
                    "confidence": round(prob * 100, 2)  # konversi ke persen
                })

        return plates
    except Exception as e:
        print(f"[DETECTOR ERROR] {str(e)}")
        traceback.print_exc()
        return []
