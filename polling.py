import telebot

bot = telebot.TeleBot("7143587146:AAEhsSJycaIrjhfXUrG7B9hjQ0sJRmxbOtk")
bot.remove_webhook()
print("Webhook removed successfully")
