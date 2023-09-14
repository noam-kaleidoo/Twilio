# השתמש בתמונת בסיס של פייתון
FROM python:3.9-slim

# הגדרת התיקייה העבודה בתוך הקונטיינר
WORKDIR /app

# העתקת הקוד שלך לתוך הקונטיינר
COPY . .

# התקנת התלות הדרושות
RUN pip install -r requirements.txt

# הגדרת הפקודה שתרוץ כאשר הקונטיינר מתחיל לרוץ
CMD ["python", "testTwilio.py"]
