from aiogram import executor

from loader import dp, db_manager
import middlewares, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    # db_manager.delete_table('users')
    # db_manager.delete_table('order_items')
    # db_manager.delete_table('product')
    # db_manager.delete_table('orders')    
    db_manager.create_table()


if __name__ == '__main__':
 executor.start_polling(dp, on_startup=on_startup)
     