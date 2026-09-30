import os
import re
from telebot import TeleBot

# Apne @BotFather se mile naye token ko yahan daalein
BOT_TOKEN = "YOUR_NEW_BOT_TOKEN_HERE"

bot = TeleBot(BOT_TOKEN)

# /start Command Handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Hi, I am calculator bot. No matter how difficult math question you ask, "
        "I will give you the answer in 2 seconds.\n\n"
        "Powered by @NOORXMODS"
    )
    bot.reply_to(message, welcome_text)

# /help Command Handler
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Hi, I am calculator bot. You can ask me any math problem you want!"
    bot.reply_to(message, help_text)

# Math Expression Evaluator and General Message Handler
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text.strip()
    
    # Mathematical expression check (Numbers and symbols only)
    # Allowed symbols: 0-9, +, -, *, /, ^, %, (, ), ., space
    if re.match(r'^[0-9\+\-\*\/\^\%\(\)\.\s]+$', text):
        try:
            # Clean expression for Python evaluation
            expression = text.replace('^', '**')
            
            # Safely evaluate math expression
            result = eval(expression, {"__builtins__": None}, {})
            
            # Send ONLY the result directly
            bot.reply_to(message, str(result))
        except Exception:
            # If math evaluation fails, send English fallback message
            bot.reply_to(message, "You cannot talk to me. I am a math bot, you can only ask me math questions.")
    else:
        # Non-math conversational text response
        bot.reply_to(message, "You cannot talk to me. I am a math bot, you can only ask me math questions.")

if __name__ == "__main__":
    bot.infinity_polling()
