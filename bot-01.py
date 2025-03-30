import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import time
import google.generativeai as genai

TELEGRAM_BOT_TOKEN = 'Telegram Bot Token'
AI_API_KEY = 'AI API KEY'

genai.configure(api_key=AI_API_KEY)
MODEL_NAME = "AI MODEL"

def timing():
    return time.strftime('%H:%M:%S on %d-%m-%y')

async def start(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(start) at {timing()}')
    reply = 'Hello! I am dèv, an AI assistant. Ask me anything.' #welcome message
    await update.message.reply_text(reply, reply_to_message_id=message_id)
    print(f'Bot : "{reply}" at {timing()}')

async def help(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(help) at {timing()}')
    reply = f'Available commands:\n/start - Start the bot.\n/translate - Translate given text into given language. Usage : /translate <lang> <text>\n/joke - Get a joke\n/quote - Get a quote\n/news - Updated news. Usage : \news <field>\n/summarize - Summarize the given content. Usage : /summarize <content>\n/time_date - Show current time and date.\n/clear - Clear all chat \n/status - Show bot status\n/model - Show model info'
    await update.message.reply_text(reply, reply_to_message_id=message_id)
    print(f'Bot : "help_text" at {timing()}')

async def get_time_date(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(time_date) at {timing()}')
    t = time.strftime('%I:%M  %p')
    date = time.strftime('%A, %d %B, %Y')
    reply = f'Current time -  {t}\n{date}'
    await update.message.reply_text(reply, reply_to_message_id = message_id)
    print(f'Bot : "system time and date" at {timing()}')

async def clear_history(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(clear_history) at {timing()}')
    if 'conversation_history' in context.chat_data:
        context.chat_data['conversation_history'] = []
    reply = 'Conversation history cleared!'
    await update.message.reply_text(reply, reply_to_message_id = message_id)
    print(f'Bot : "{reply}" at {timing()}')

async def translate_text(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(translate) at {timing()}')
    if not context.args:
        await update.message.reply_text('Please provide text to translate. Usage: /translate <lang> <text>')
        return
    text = context.args[1:]
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = f"Translate this text to {context.args[0]}: {text}"
        response = model.generate_content(prompt)
        await update.message.reply_text(f'Translating by dèv....', reply_to_message_id = message_id)
        await update.message.reply_text(response.text, reply_to_message_id = message_id)
        print(f'Bot : {response.text} at {timing()}')
    except Exception as e:
        await update.message.reply_text(f'Translation error: {str(e)}', reply_to_message_id = message_id)

async def get_status(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(status) at {timing()}')
    status = f"Bot Status:\nAI Model: {MODEL_NAME}\nActive: Yes\nLatency: {time.time():.2f}s"
    await update.message.reply_text(status, reply_to_message_id = message_id)
    print(f'Bot : {status} at {timing()}')

async def get_model_info(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(model_info) at {timing()}')
    model_info = f"Current Model: {MODEL_NAME}\nProvider: Google Generative AI\nCapabilities: Text generation, translation, conversation"
    await update.message.reply_text(model_info, reply_to_message_id = message_id)
    print(f'Bot : {model_info} at {timing()}')

async def get_joke(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(joke) at {timing()}')
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content("Tell me a joke, another joke")
        await update.message.reply_text(response.text, reply_to_message_id = message_id)
        print(f'Bot : "{response.text}" at {timing()}')
    except Exception as e:
        await update.message.reply_text(f'Error getting joke: {str(e)}', reply_to_message_id = message_id)

async def get_quote(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(quote) at {timing()}')
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content("Share an inspiring quote with its author.")
        await update.message.reply_text(response.text, reply_to_message_id = message_id)
        print(f'Bot : "{response.text}" at {timing()}')
    except Exception as e:
        await update.message.reply_text(f'Error getting quote: {str(e)}', reply_to_message_id = message_id)
        print('ERROR in quote function')

async def get_news(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(news) at {timing()}')
    if not context.args: 
        await update.message.reply_text('Please provide specific field for news. Usage : /news <field>')
        return
    field = context.args[0]
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        text = f"Today's news on {field}."
        response = model.generate_content(text)
        await update.message.reply_text(response.text, reply_to_message_id = message_id)
        print(f'Bot : "{response.text}" at {timing()}')
    except Exception as e:
        await update.message.reply_text(f'Error getting news: {str(e)}', reply_to_message_id = message_id)

async def summarize(update, context):
    user = update.effective_user
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : command(summarize) at {timing()}')
    if not context.args: 
        await update.message.reply_text('Please provide proper syntax for summarize. Usage : /summarize <content>')
        return
    paragraph = context.args[1:]
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(f"Please summarize this content : {paragraph}. And make points for better understanding. ")
        await update.message.reply_text(response.text, reply_to_message_id = message_id)
        print(f'Bot : "{response.text}" at {timing()}')
    except Exception as e:
        await update.message.reply_text(f'Error summarising paragraph : {str(e)}', reply_to_message_id = message_id)

async def handle_message(update, context):
    user = update.effective_user
    user_message = update.message.text
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    print(f'\nuser({user.id}) : "{user_message}" at {timing()}')
    await context.bot.send_chat_action(chat_id=chat_id, action="typing")

    if 'conversation_history' not in context.chat_data:
        context.chat_data['conversation_history'] = []

    context.chat_data['conversation_history'].append({"role": "user", "parts": [user_message]})

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(context.chat_data['conversation_history'])

        if response.text:
            response_text = response.text
            max_message_length = 4000

            if len(response_text) > max_message_length:
                for i in range(0, len(response_text), max_message_length):
                    split_message = response_text[i:i + max_message_length]
                    await update.message.reply_text(split_message, reply_to_message_id=message_id)
                    time.sleep(0.5)
            else:
                await update.message.reply_text(response_text, reply_to_message_id=message_id)

            context.chat_data['conversation_history'].append({"role": "model", "parts": [response.text]})
            print(f'Bot : "{response_text}" at {timing()}')
        else:
            reply_text = "Sorry, I couldn't understand that. dèv returned an empty response."
            await update.message.reply_text(reply_text, reply_to_message_id=message_id)
            print(f'Bot : "{reply_text}" at {timing()}')

    except Exception as e:
        print(f"Error: {e}")
        reply_text = 'An error occurred while processing your request.'
        await update.message.reply_text(reply_text, reply_to_message_id=message_id)

async def error(update, context):
    message_id = update.message.message_id
    print(f'Update {update} caused error {context.error}')
    if update and update.message:
        await update.message.reply_text('There is some error in server or in system. Please try again later.', reply_to_message_id = message_id)

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("translate", translate_text))
    app.add_handler(CommandHandler("joke", get_joke))
    app.add_handler(CommandHandler("quote", get_quote))
    app.add_handler(CommandHandler("news", get_news))
    app.add_handler(CommandHandler("summarize", summarize))
    app.add_handler(CommandHandler("time&date", get_time_date))
    app.add_handler(CommandHandler("status", get_status))
    app.add_handler(CommandHandler("model", get_model_info))
    app.add_handler(CommandHandler("clear", clear_history))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)

    print('Polling....')
    try:
        app.run_polling(
            poll_interval=2,
            drop_pending_updates=True,
            allowed_updates=["message"],
            close_loop=True,
            stop_signals=None
        )
    except Exception as e:
        print(f"Polling error: {e}")
    finally:
        app.stop()
        app.shutdown()

if __name__ == '__main__':
    main()
