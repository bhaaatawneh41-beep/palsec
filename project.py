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
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 1. استخراج بيانات المستخدم
    user = update.message.from_user
    name = user.first_name  # الاسم الأول للمستخدم
    username = user.username if user.username else "لا يوجد يوزرنيم" # اليوزرنيم إذا كان موجوداً
    
    # 2. الحصول على نص الرسالة
    text = update.message.text.strip()
    
    # 3. صياغة الرد (مع دمج اسم المستخدم)
    response_header = f"أهلاً {name} (@{username})، "
    
    if "طلب صيانة" in text:
        await update.message.reply_text(f"{response_header}يرجى تزويدنا بتفاصيل المشكلة وسنتواصل معك.")
    elif "تركيب كاميرات" in text:
        await update.message.reply_text(f"{response_header}يسعدنا خدمتك! هل لديك موقع محدد؟")
    elif "خدمات الشبكات" in text:
        await update.message.reply_text(f"{response_header}نقدم حلول شبكات متكاملة، هل تحتاج لاستشارة؟")
    elif "الموقع" in text:
        await update.message.reply_text(f"{response_header}يمكنك العثور على موقعنا هنا: [الخليل - بيت كاحل - 0599523164]")
    elif "الأسعار" in text:
        await update.message.reply_text(f"{response_header}سوف نتواصل معك لتقديم قائمة الأسعار.")
    else:
        # إذا كانت رسالة نصية عامة، نكررها مع اسم المستخدم
        await update.message.reply_text(f"{response_header}تم استلام رسالتك: {text}")
# 5. تشغيل البوت
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot is running...")
    application.run_polling()