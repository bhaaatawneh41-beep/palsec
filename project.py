import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
# 1. ضع التوكن الخاص بك هنا
TOKEN =  os.environ.get("TOKEN")
# 2. تعريف الأزرار
def get_main_keyboard():
    keyboard = [
        [KeyboardButton("طلب صيانة 🛠️"), KeyboardButton("تركيب كاميرات 📷")],
        [KeyboardButton("خدمات الشبكات 🌐"), KeyboardButton("الموقع 📍")],
        [KeyboardButton("الأسعار 💰")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# 3. دالة البداية (start)
async def start(update, context):
    await update.message.reply_text(
        "أهلاً بك في PALSEC Support! كيف يمكننا مساعدتك اليوم؟",
        reply_markup=get_main_keyboard()
    )

# 4. دالة معالجة الأزرار والنصوص (handle)
async def handle(update, context):
    user_text = update.message.text
    
    if user_text == "طلب صيانة 🛠️":
        await update.message.reply_text("أهلاً بك، تم استلام طلب الصيانة الخاص بك 🛠️. سنقوم بالتواصل معك قريباً.")
    
    elif user_text == "تركيب كاميرات 📷":
        await update.message.reply_text("تم اختيار تركيب الكاميرات 📷. أخبرنا بمزيد من التفاصيل أو أرسل صورة العطل.")
        
    elif user_text == "الموقع 📍":
        await update.message.reply_text("موقعنا: الخليل - فلسطين 📍")
        
    else:
        await update.message.reply_text("تم استلام رسالتك: " + user_text)

# 5. تشغيل البوت
if __name__ == '__main__':
    # تشغيل الخادم الوهمي في الخلفية (ضروري لبقاء البوت على Render)
   import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 1. ضع التوكن هنا
TOKEN = "8342410932:AAEtLjBkZsQRHy2bXGIJhfd4joypY4w7X5o"

# 2. تعريف الدوال
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! البوت يعمل بنجاح.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("لقد وصلتني رسالتك!")

# --- كود الخادم (للحفاظ على عمل البوت) ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# --- تشغيل البوت ---
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    # إضافة المعالجات
    application.add_handler(CommandHandler('start', start))
    # هنا قمنا بتصحيح السطر ليكون 'handle_message' وليس 'msg_handler'
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot is running...")
    application.run_polling()