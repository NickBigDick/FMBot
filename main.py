from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands
from telebot import custom_filters
from handlers.default_heandlers import auth


if __name__ == '__main__':
    auth.check_auth_table()

    set_default_commands(bot)
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(custom_filters.IsDigitFilter())
    # bot.webhook_listener51943
    # app.run()
    bot.infinity_polling()




