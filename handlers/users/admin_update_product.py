from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.admin_main_menu import admin_main_menu
from keyboards.inline.change_product import *

from loader import dp, db_manager
from states.change_product_state import UpdateProduct


@dp.message_handler(text="⬅️ Orqaga", chat_id=ADMINS, state="*")
async def stickers_menu(message: types.Message, state: FSMContext):
    text = "Bosh menyuga xush kelibsiz😊"
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_change_photo.filter(action="change_product_photo"),
                           state="all-product-state")
async def admin_change_photo_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    await state.update_data(product_id=product_id)
    text = "Yangi rasmni kiriting.📸"
    await call.message.answer(text=text)
    await UpdateProduct.photo.set()


@dp.message_handler(state=UpdateProduct.photo, content_types=types.ContentType.PHOTO)
async def update_photo_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    photo = message.photo[-1].file_id

    if db_manager.update_admin_sticker(product_id, "photo", photo):
        text = "Rasm yangilandi.📸"
    else:
        text = "Xatolik bor."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_change_name.filter(action="change_product_name"),
                           state="all-product-state")
async def admin_change_photo_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    await state.update_data(product_id=product_id)
    text = "Yangi nomni kiriting.😊"
    await call.message.answer(text=text)
    await UpdateProduct.product_name.set()


@dp.message_handler(state=UpdateProduct.product_name)
async def update_photo_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    product_name = message.text

    if db_manager.update_admin_sticker(product_id, "product_name", product_name):
        text = "Nom yangilandi.😊"
    else:
        text = "Xatolik bor."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_change_price.filter(action="change_product_price"),
                           state="all-product-state")
async def admin_change_photo_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    await state.update_data(product_id=product_id)
    text = "Yangi narxini kiriting.😊"
    await call.message.answer(text=text)
    await UpdateProduct.price.set()


@dp.message_handler(state=UpdateProduct.price)
async def update_photo_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    price = message.text

    if db_manager.update_admin_sticker(product_id, "price", price):
        text = "Narx yangilandi.😊"
    else:
        text = "Xatolik bor."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_change_description.filter(action="change_product_description"),
                           state="all-product-state")
async def admin_change_photo_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    await state.update_data(product_id=product_id)
    text = "Yangi ma'lumotni kiriting.😊"
    await call.message.answer(text=text)
    await UpdateProduct.description.set()


@dp.message_handler(state=UpdateProduct.description)
async def update_photo_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    description = message.text

    if db_manager.update_admin_sticker(product_id, "description", description):
        text = "Ma'lumot yangilandi.😊"
    else:
        text = "Xatolik bor."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_change_quantity.filter(action="change_product_quantity"),
                           state="all-product-state")
async def admin_change_photo_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    await state.update_data(product_id=product_id)
    text = "Yangi ma'lumotni kiriting.😊"
    await call.message.answer(text=text)
    await UpdateProduct.quantity.set()


@dp.message_handler(state=UpdateProduct.quantity)
async def update_photo_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    product_id = data.get('product_id')
    quantity = message.text

    if db_manager.update_admin_sticker(product_id, "quantity", quantity):
        text = "Ma'lumot yangilandi.😊"
    else:
        text = "Xatolik bor."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.callback_query_handler(admin_product_delete.filter(action="change_product_delete"),
                           state="all-product-state")
async def admin_change_delete_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    product_id = callback_data.get('product_id')
    if db_manager.delete_product(product_id):
        text = "Ma'lumot ochirildi."
    else:
        text = "Xatolik bor."
    await call.message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()
