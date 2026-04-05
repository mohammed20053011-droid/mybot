from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# 🔴 حط التوكن هنا
TOKEN = "8655578936:AAH2AW08yMXJnDZU4Bgi-QAxt7o02J7pvpU"

# ===== الأزرار الرئيسية =====
keyboard = [
    ["📸 لجنة التصوير والتوثيق"],
    ["🎨 لجنة التصميم"],
    ["📢 اللجنة الإلكترونية"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ===== /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بيك في بوت المنظمة\nاختار اللجنة:",
        reply_markup=reply_markup
    )

# ===== التعامل مع الرسائل =====
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # 📸 التصوير
    if text == "📸 لجنة التصوير والتوثيق":
        await update.message.reply_text(
            "📝 استمارة التصوير والتوثيق:\n\n"
            "🏢 المكتب:\n"
            "👤 اسم المسؤول:\n"
            "📱 التواصل:\n"
            "📅 تاريخ الطلب:\n"
            "📆 تاريخ التنفيذ:\n"
            "🎯 تفاصيل التغطية:\n\n"
            "✍️ اكتب كل البيانات في رسالة واحدة وارسلها هنا"
        )

    # 🎨 التصميم
    elif text == "🎨 لجنة التصميم":
        await update.message.reply_text(
            "📝 استمارة التصميم:\n\n"
            "🏢 المكتب:\n"
            "👤 المسؤول:\n"
            "📱 التواصل:\n"
            "📅 تاريخ الطلب:\n"
            "📆 تاريخ التسليم:\n"
            "🎯 تفاصيل التصميم:\n\n"
            "✍️ اكتب الطلب كامل وارسلو هنا"
        )

    # 📢 الإلكترونية
    elif text == "📢 اللجنة الإلكترونية":
        await update.message.reply_text(
            "📝 استمارة البوستات:\n\n"
            "🔷 اكتب موضوع البوست\n"
            "🔷 الفكرة الأساسية\n"
            "🔷 الفئة المستهدفة\n"
            "🔷 أي تفاصيل إضافية\n\n"
            "✍️ أرسل الطلب كامل هنا"
        )

    # أي رسالة ثانية
    else:
        await update.message.reply_text("✔️ تم استلام طلبك، جاري المعالجة...")

# ===== تشغيل البوت =====
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
