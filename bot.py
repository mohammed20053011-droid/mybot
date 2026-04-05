from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8655578936:AAH2AW08yMXJnDZU4Bgi-QAxt7o02J7pvpU"
ADMIN_CHAT_ID = "5546714606"

user_type = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["📸 التصوير"], ["🎨 التصميم"], ["💻 الإلكترونية"]]

    await update.message.reply_text(
        "👋 اختر القسم:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.message.from_user.id

    if text == "📸 التصوير":
        user_type[user_id] = "photo"
        await update.message.reply_text("📸 اكتب الفورم كامل وارسلو مرة واحدة")

    elif text == "🎨 التصميم":
        user_type[user_id] = "design"
        await update.message.reply_text("🎨 اكتب الفورم كامل وارسلو مرة واحدة")

    elif text == "💻 الإلكترونية":
        user_type[user_id] = "electronic"
        await update.message.reply_text("💻 اكتب الفورم كامل وارسلو مرة واحدة")

async def receive_form(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    if user_id in user_type:
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"📩 طلب جديد:\n\n{text}"
        )
        await update.message.reply_text("✅ تم الاستلام")
    else:
        await update.message.reply_text("اضغط /start")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
app.add_handler(MessageHandler(filters.TEXT, receive_form))

print("Bot running...")
app.run_polling()
