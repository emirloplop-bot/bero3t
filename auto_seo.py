# auto_seo.py
import requests, time, random
from datetime import datetime

class Bero3tSEO:
    def __init__(self):
        self.token = "6888524885:AAEHvwSRkNB2mY5v5izUhv_bTAMoDtJp83A"
        self.chat_id = "5451721858"
        self.sites = [
            "guns.lol/bero3t",
            "linktr.ee/bero3t",
            "instagram.com/f1formula_",
            "tiktok.com/@berouser",
            "youtube.com/@bero3t"
        ]
    
    def telegram(self, msg):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        requests.post(url, json={"chat_id": self.chat_id, "text": msg, "parse_mode": "HTML"})
    
    def ping_google(self):
        for site in self.sites:
            try:
                requests.get(f"https://www.google.com/ping?sitemap=https://{site}")
                self.telegram(f"✅ Google ping: {site}")
            except:
                pass
            time.sleep(2)
    
    def backlink(self):
        sites = ["reddit.com", "quora.com", "dev.to", "medium.com", "linkedin.com"]
        for site in sites:
            self.telegram(f"🔗 Backlink: {site} → guns.lol/bero3t")
            time.sleep(1)
    
    def report(self):
        now = datetime.now()
        msg = f"""
📊 <b>BERO3T RAPOR</b> - {now.strftime('%d.%m.%Y %H:%M')}

✅ <b>Aktif:</b>
• guns.lol/bero3t
• linktr.ee/bero3t
• instagram.com/f1formula_
• tiktok.com/@berouser
• youtube.com/@bero3t

🚀 <b>Durum:</b> Optimizasyon aktif
🎯 <b>Hedef:</b> Google ilk sayfa

#bero3t
"""
        self.telegram(msg)
    
    def run(self):
        self.telegram("🚀 <b>bero3t bot başladı!</b>")
        while True:
            self.ping_google()
            self.backlink()
            self.report()
            time.sleep(21600)  # 6 saat

if __name__ == "__main__":
    Bero3tSEO().run()
