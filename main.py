import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return '<div dir="rtl">🤖 سيرفر بوت واتساب للعطور يعمل بنجاح على السحابة!</div>'

@app.route("/whatsapp-webhook", methods=["POST"])
def whatsapp_webhook():
    incoming_data = request.json
    print("تم استلام بيانات من واتساب بنجاح:", incoming_data)
    reply_text = "✨ أهلاً بك! تم استلام رابط العطر وفحصه بنجاح."
    return jsonify({"status": "success", "message": reply_text}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
