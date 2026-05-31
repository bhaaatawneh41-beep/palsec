from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 1. إعدادات البوت والربط بحسابك الشخصي
TOKEN = "8342410932:AAEtLjBkZsQRHy2bXGIJhfd4joypY4w7X5o"
MY_CHAT_ID = 6456568331  

# 2. تصميم أزرار القائمة الرئيسية
keyboard = [
    ["📸 تركيب كاميرات", "🛠️ طلب صيانة"],
    ["🌐 خدمات الشبكات", "📞 التواصل المباشر : 0569563879"],
    ["📍 موقعنا", "💰 الأسعار"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# 3. دالة الترحيب عند الضغط على /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "🔒 أهلاً بك في PALSEC Support\n\nنوفر خدمات تركيب الكاميرات، أنظمة الحماية، والشبكات الذكية.\n\n👇 يرجى اختيار الخدمة المطلوبة من القائمة أدناه:"
    await update.message.reply_text(text, reply_markup=reply_markup)

# 4. دالة معالجة الرسائل والطلبات وإرسالها لهاتفك
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # .strip() تضمن إزالة أي مسافات زائدة أو مخفية من أطراف النص
    msg = update.message.text.strip()
    user = update.message.from_user

    # تجهيز تفاصيل حساب الزبون
    username = f"@{user.username}" if user.username else "لا يوجد يوزر نيم"
    customer_info = f"👤 الزبون: {user.full_name}\n🆔 معرف الحساب: {username}"

    # قاموس الردود الثابتة للأزرار (متطابق 100% مع أزرار المصفوفة فوق)
    responses = {
        "📸 تركيب كاميرات": "يرجى إرسال تفاصيل الموقع وعدد الكاميرات 📸",
        "🛠️ طلب صيانة": "أرسل صورة العطل أو وصف المشكلة 🛠️",
        "🌐 خدمات الشبكات": "نوفر تمديد وبرمجة شبكات وإنترنت 🌐",
        "📞 التواصل المباشر : 0569563879": "يمكنك الاتصال بنا مباشرة عبر الرقم: 0569563879 📞",
        "📍 موقعنا": "الخليل - فلسطين 📍",
        "💰 الأسعار": "الأسعار تختلف حسب نوع الخدمة المطلوب تنفيذها 💰"
    }

    # إذا ضغط الزبون على زر من القائمة الرئيسية، نرد عليه بالجواب المخصص له فقط
    if msg in responses:
        await update.message.reply_text(responses[msg])
    
    # إذا كتب الزبون تفاصيل (مثل: الخليل - بيت كاحل - عدد 4 كاميرات)
    else:
        # أولاً: رد تلقائي للزبون لتأكيد الاستلام
        await update.message.reply_text(
            "✅ تم استلام تفاصيلك بنجاح، وسيتواصل معك الدعم الفني فوراً.\n\n👇 يمكنك اختيار خدمة أخرى من القائمة:",
            reply_markup=reply_markup
        )
        
        # ثانياً: إرسال تفاصيل الطلب إلى حسابك الشخصي
        try:
            alert_text = f"🔔 **وصلك طلب جديد من البوت!**\n\n{customer_info}\n\n📝 **نص الرسالة:**\n{msg}"
            await context.bot.send_message(chat_id=MY_CHAT_ID, text=alert_text)
        except Exception as e:
            print(f"حدث خطأ أثناء إرسال الإشعار للمشرف: {e}")

# 5. تشغيل وتفعيل البوت
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle))

print("Bot Running...")
app.run_polling()