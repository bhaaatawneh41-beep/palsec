import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 1. إعدادات البوت (تأكد من إضافة TOKEN في Render Environment)
TOKEN = os.environ.get("TOKEN")

# 2. تعريف الأزرار
def get_main_keyboard():
    keyboard = [
        [KeyboardButton("🛠️ طلب صيانة"), KeyboardButton("📷 تركيب كاميرات")],
        [KeyboardButton("🌐 خدمات الشبكات"), KeyboardButton("📍 الموقع")],
        [KeyboardButton("💰 الأسعار")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# 3. دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك في PALSEC Support! كيف يمكننا مساعدتك اليوم؟", reply_markup=get_main_keyboard())

# 4. دالة معالجة النصوص (تأكد أنها تبدأ من أول السطر بدون مسافات)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    
    if "طلب صيانة" in text:
        await update.message.reply_text("أهلاً بك، يرجى تزويدنا بتفاصيل المشكلة.")
    elif "تركيب كاميرات" in text:
        await update.message.reply_text("يسعدنا خدمتك! هل لديك موقع محدد؟")
    elif "خدمات الشبكات" in text:
        await update.message.reply_text("نقدم حلول شبكات متكاملة، هل تحتاج لاستشارة؟")
    elif "الموقع" in text:
        await update.message.reply_text("يمكنك العثور على موقعنا هنا: [رابط موقعك]")
    elif "الأسعار" in text:
        await update.message.reply_text("يمكنك الاطلاع على قائمة الأسعار في ملف PDF.")
    else:
        await update.message.reply_text("تم استلام رسالتك: " + text)

# 5. تشغيل البوت
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot is running...")
    application.run_polling()