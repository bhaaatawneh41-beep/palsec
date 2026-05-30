from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

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
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle))
    
    print("البوت يعمل الآن ومستعد لاستقبال الرسائل...")
    app.run_polling()