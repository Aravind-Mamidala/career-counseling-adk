# test_firebase.py

from firebase_config import db

def test_connection():
    try:
        doc_ref = db.collection("test").document("connection_check")
        doc_ref.set({"status": "connected!"})
        print("✅ Firebase connected successfully!")
    except Exception as e:
        print("❌ Firebase connection failed:", e)

test_connection()
