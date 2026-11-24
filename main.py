import requests
from datetime import datetime

TOKEN = "9121087220:AAFYStUqG9IftgELr-Wf7oOOre6WtfuS2no"
CHANNEL = "-1003937196719"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHANNEL, "text": msg, "parse_mode": "HTML"})

text = f"""🕷️ <b>BMG SPIDER - RELATORIOS 10-Q</b>
📅 {datetime.now().strftime('%d/%m/%Y 07:00 BRT')}

🏢 Ultimos 10-Q na SEC:
- AAPL - $97.7B
- MSFT - $61.8B
- NVDA - $26B

🔗 Extracao automatica SEC EDGAR
<i>By @bmg_spider_10q_bot</i>
"""

send(text)
