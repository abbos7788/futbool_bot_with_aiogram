from config import TOKEN 
import logging
from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import mysql.connector
from aiogram.types import Message, CallbackQuery
import datetime

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="nazarov_7788",
  port="3306",
  database="youtube"
)

cursor = db.cursor()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


# cursor.execute("CREATE TABLE time_table_2 (id INT AUTO_INCREMENT PRIMARY KEY, user_id VARCHAR(255), time VARCHAR(255), comment VARCHAR(255), time_now VARCHAR(255))")







@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("<b>Assalomu Alaykum </b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_inline_2)


@dp.message_handler(text="🕑 Vaqtlarni ko'rish")
async def menu_1(message: types.Message):
    sql = "SELECT * FROM time_table_2 WHERE user_id ='{}'".format(f"1")
    cursor.execute(sql)
    myresult = cursor.fetchall()
    res = """<b>🔰 Bron qilingan vaqtlar</b>\n\n"""
    for k in myresult:
        print(k)
        # res += f"""🤵 User id: <b>{k[0]}\n🔰 Time: {k[1]}\n🗨️ Comment: {k[2]}\n🕝 Comment time: {k[3]}</b>\n\n"""
        res += f"""<b>🕝 Time: {k[2]}\n\n</b>"""
    await message.answer(res, parse_mode="HTML", reply_markup=bosh_sahifa_inline_2)

@dp.message_handler(text="📞 Aloqaga chiqish")
async def menu_2(message: types.Message):
    await message.answer("<b>Aloqa: +998 94-123-45-67</b>",parse_mode = 'HTML',reply_markup = bosh_sahifa_inline_2)

@dp.message_handler(text="🔰 To'lov")
async def menu_3(message: types.Message):
    await message.answer("""<b>Karta: 9860123456789</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_inline_2)

@dp.message_handler(text="🏡 Bosh sahifa")
async def menu_2(message: types.Message):
    await message.answer("<b>Menu</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_inline_2)















@dp.message_handler(text="⚜️ Admin page")
async def send_welcome_admin(message: types.Message):
    if f"{message.chat.id}" == "276482229" or f"{message.chat.id}" == "5158944832" or f"{message.chat.id}" == "5073296253":
       await message.answer(f"<b>Assalomu Alaykum! {message.from_user.full_name} || Admin page</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_inline_4)
    else:
       await message.answer("<b>Kechirasiz, Ushbu bo'limga faqat adminlik huquqi bor odam kirishi mumkin!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_inline_2)
    


@dp.message_handler(text="🕑 Vaqtni ko'rish")
async def menu_1(message: types.Message):
    sql = "SELECT * FROM time_table_2 WHERE user_id ='{}'".format(f"1")
    cursor.execute(sql)
    myresult = cursor.fetchall()
    res = """<b>🔰 Bron qilingan vaqtlar</b>\n\n"""
    for k in myresult:
        print(k)
        res += f"""🤵 User id: <b>{k[1]}\n🔰 Time: {k[2]}\n🗨️ Comment: {k[3]}\n🕝 Comment time: {k[4]}</b>\n\n"""
        # res += f"""<b>🕝 Time: {k[1]}\n\n</b>"""
    await message.answer(res, parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)


@dp.message_handler(text="➕ Add")
async def welcome_admin(message: types.Message):
    await message.answer("""<b>Welcome to the Admin panel!</b>""" , parse_mode = 'HTML')
    await message.answer("""<b>Choose time limits!</b>""" , parse_mode = 'HTML', reply_markup=bosh_sahifa_inline_1)

class Auth_2(StatesGroup):
    text_box_2 = State()

class Auth_11(StatesGroup):
    text_box_2 = State()

class Auth_12(StatesGroup):
    text_box_2 = State()

class Auth_13(StatesGroup):
    text_box_2 = State()

class Auth_14(StatesGroup):
    text_box_2 = State()

class Auth_15(StatesGroup):
    text_box_2 = State()

class Auth_16(StatesGroup):
    text_box_2 = State()

class Auth_17(StatesGroup):
    text_box_2 = State()

class Auth_18(StatesGroup):
    text_box_2 = State()

class Auth_19(StatesGroup):
    text_box_2 = State()

class Auth_20(StatesGroup):
    text_box_2 = State()

class Auth_21(StatesGroup):
    text_box_2 = State()

class Auth_22(StatesGroup):
    text_box_2 = State()

class Auth_23(StatesGroup):
    text_box_2 = State()

class Auth_24(StatesGroup):
    text_box_2 = State()

class Auth_25(StatesGroup):
    text_box_2 = State()

class Auth_26(StatesGroup):
    text_box_2 = State()

class Auth_27(StatesGroup):
    text_box_2 = State()

class Auth_28(StatesGroup):
    text_box_2 = State()

class Auth_29(StatesGroup):
    text_box_2 = State()

class Auth_30(StatesGroup):
    text_box_2 = State()

class Auth_31(StatesGroup):
    text_box_2 = State()

class Auth_32(StatesGroup):
    text_box_2 = State()

class Auth_33(StatesGroup):
    text_box_2 = State()







class Auth_34(StatesGroup):
    text_box_2 = State()

class Auth_35(StatesGroup):
    text_box_2 = State()

class Auth_36(StatesGroup):
    text_box_2 = State()

class Auth_37(StatesGroup):
    text_box_2 = State()

class Auth_38(StatesGroup):
    text_box_2 = State()

class Auth_39(StatesGroup):
    text_box_2 = State()

class Auth_40(StatesGroup):
    text_box_2 = State()

class Auth_41(StatesGroup):
    text_box_2 = State()

class Auth_42(StatesGroup):
    text_box_2 = State()


class Auth_43(StatesGroup):
    text_box_2 = State()

class Auth_44(StatesGroup):
    text_box_2 = State()

class Auth_45(StatesGroup):
    text_box_2 = State()

class Auth_46(StatesGroup):
    text_box_2 = State()

class Auth_47(StatesGroup):
    text_box_2 = State()

class Auth_48(StatesGroup):
    text_box_2 = State()

class Auth_49(StatesGroup):
    text_box_2 = State()

class Auth_50(StatesGroup):
    text_box_2 = State()

class Auth_51(StatesGroup):
    text_box_2 = State()

class Auth_52(StatesGroup):
    text_box_2 = State()

class Auth_53(StatesGroup):
    text_box_2 = State()



#PART 1

@dp.message_handler(text="01:00-02:00", state="*")
async def ab_1(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_2.text_box_2.set()

@dp.message_handler(state=Auth_2.text_box_2)
async def ab_2(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "01:00-02:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    

@dp.message_handler(text="02:00-03:00", state="*")
async def ab_3(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_11.text_box_2.set()

@dp.message_handler(state=Auth_11.text_box_2)
async def ab_4(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "02:00-03:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="03:00-04:00", state="*")
async def ab_5(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_12.text_box_2.set()

@dp.message_handler(state=Auth_12.text_box_2)
async def ab_6(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "03:00-04:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="05:00-06:00", state="*")
async def ab_7(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_13.text_box_2.set()

@dp.message_handler(state=Auth_13.text_box_2)
async def ab_8(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "05:00-06:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    
#PART 2
@dp.message_handler(text="09:00-10:00", state="*")
async def ab_9(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_14.text_box_2.set()

@dp.message_handler(state=Auth_14.text_box_2)
async def ab_10(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "09:00-10:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    

@dp.message_handler(text="11:00-12:00", state="*")
async def ab_11(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_15.text_box_2.set()

@dp.message_handler(state=Auth_15.text_box_2)
async def ab_12(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "11:00-12:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="13:00-14:00", state="*")
async def ab_13(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_16.text_box_2.set()

@dp.message_handler(state=Auth_16.text_box_2)
async def ab_14(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "13:00-13:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="15:00-16:00", state="*")
async def ab_15(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_17.text_box_2.set()

@dp.message_handler(state=Auth_17.text_box_2)
async def ab_16(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "15:00-16:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)


#PART 3

@dp.message_handler(text="17:00-18:00", state="*")
async def ab_17(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_18.text_box_2.set()

@dp.message_handler(state=Auth_18.text_box_2)
async def nameab_18(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "17:00-18:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    

@dp.message_handler(text="19:00-20:00", state="*")
async def ab_19(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_19.text_box_2.set()

@dp.message_handler(state=Auth_19.text_box_2)
async def ab_20(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "19:00-20:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="21:00-22:00", state="*")
async def ab_21(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_20.text_box_2.set()

@dp.message_handler(state=Auth_20.text_box_2)
async def ab_22(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "21:00-22:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="23:00-24:00", state="*")
async def ab_23(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_21.text_box_2.set()

@dp.message_handler(state=Auth_21.text_box_2)
async def ab_24(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "23:00-24:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



#PART 4

@dp.message_handler(text="01:30-02:30", state="*")
async def ab_25(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_22.text_box_2.set()

@dp.message_handler(state=Auth_22.text_box_2)
async def ab_26(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "01:30-02:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    

@dp.message_handler(text="02:30-03:30", state="*")
async def ab_27(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_23.text_box_2.set()

@dp.message_handler(state=Auth_23.text_box_2)
async def ab_28(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "02:30-03:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="03:30-04:30", state="*")
async def ab_29(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_24.text_box_2.set()

@dp.message_handler(state=Auth_24.text_box_2)
async def ab_30(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "03:30-04:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi! </b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="05:30-06:30", state="*")
async def ab_31(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_25.text_box_2.set()

@dp.message_handler(state=Auth_25.text_box_2)
async def ab_32(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "05:30-06:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)


 #PART 5


@dp.message_handler(text="09:30-10:30", state="*")
async def ab_33(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_26.text_box_2.set()

@dp.message_handler(state=Auth_26.text_box_2)
async def ab_34(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "09:30-10:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    

@dp.message_handler(text="11:30-12:30", state="*")
async def ab_35(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_27.text_box_2.set()

@dp.message_handler(state=Auth_27.text_box_2)
async def ab_36(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "11:30-12:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="13:30-14:30", state="*")
async def ab_37(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_28.text_box_2.set()

@dp.message_handler(state=Auth_28.text_box_2)
async def ab_38(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "13:30-14:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="15:30-16:30", state="*")
async def ab_39(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_29.text_box_2.set()

@dp.message_handler(state=Auth_29.text_box_2)
async def ab_40(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "15:30-16:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)


#PART 6


@dp.message_handler(text="17:30-18:30", state="*")
async def ab_41(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_30.text_box_2.set()

@dp.message_handler(state=Auth_30.text_box_2)
async def ab_42(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "17:30-18:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    

@dp.message_handler(text="19:30-20:30", state="*")
async def ab_43(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_31.text_box_2.set()

@dp.message_handler(state=Auth_31.text_box_2)
async def ab_44(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "19:30-20:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="21:30-22:30", state="*")
async def ab_45(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_32.text_box_2.set()

@dp.message_handler(state=Auth_32.text_box_2)
async def ab_46(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "21:30-22:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="23:30-24:30", state="*")
async def ab_47(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_33.text_box_2.set()

@dp.message_handler(state=Auth_33.text_box_2)
async def ab_48(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "23:30-24:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

#PART 7

@dp.message_handler(text="04:00-05:00", state="*")
async def ab_49(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_34.text_box_2.set()

@dp.message_handler(state=Auth_34.text_box_2)
async def ab_50(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "04:00-05:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    

@dp.message_handler(text="10:00-11:00", state="*")
async def ab_51(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_35.text_box_2.set()

@dp.message_handler(state=Auth_35.text_box_2)
async def ab_52(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "10:00-11:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="12:00-13:00", state="*")
async def ab_53(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_36.text_box_2.set()

@dp.message_handler(state=Auth_36.text_box_2)
async def ab_54(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "12:00-13:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="14:00-15:00", state="*")
async def ab_55(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_37.text_box_2.set()

@dp.message_handler(state=Auth_37.text_box_2)
async def ab_56(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "14:00-15:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



#PART 8


@dp.message_handler(text="16:00-17:00", state="*")
async def ab_57(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_38.text_box_2.set()

@dp.message_handler(state=Auth_38.text_box_2)
async def ab_58(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "16:00-17:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi! </b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    

@dp.message_handler(text="18:00-19:00", state="*")
async def ab_59(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_39.text_box_2.set()

@dp.message_handler(state=Auth_39.text_box_2)
async def ab_60(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "18:00-19:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="20:00-21:00", state="*")
async def ab_61(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_40.text_box_2.set()

@dp.message_handler(state=Auth_40.text_box_2)
async def ab_62(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "20:00-21:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi! </b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="22:00-23:00", state="*")
async def ab_63(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_41.text_box_2.set()

@dp.message_handler(state=Auth_41.text_box_2)
async def ab_64(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "22:00-23:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

@dp.message_handler(text="24:00-01:00", state="*")
async def ab_65(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_42.text_box_2.set()

@dp.message_handler(state=Auth_42.text_box_2)
async def ab_66(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "24:00-01:00", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)


#PART 9


@dp.message_handler(text="04:30-05:30", state="*")
async def ab_67(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_43.text_box_2.set()

@dp.message_handler(state=Auth_44.text_box_2)
async def ab_68(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "04:30-05:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    

@dp.message_handler(text="10:30-11:30", state="*")
async def ab_69(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_45.text_box_2.set()

@dp.message_handler(state=Auth_45.text_box_2)
async def ab_70(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "10:30-11:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="12:30-13:30", state="*")
async def ab_71(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_46.text_box_2.set()

@dp.message_handler(state=Auth_46.text_box_2)
async def ab_72(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "12:30-13:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi! </b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="14:30-15:30", state="*")
async def ab_73(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_47.text_box_2.set()

@dp.message_handler(state=Auth_47.text_box_2)
async def ab_74(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "14:30-15:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

@dp.message_handler(text="16:30-17:30", state="*")
async def ab_75(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_49.text_box_2.set()

@dp.message_handler(state=Auth_49.text_box_2)
async def ab_76(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "16:30-17:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi! </b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)


#PART 10


@dp.message_handler(text="18:30-19:30", state="*")
async def ab_77(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_50.text_box_2.set()

@dp.message_handler(state=Auth_50.text_box_2)
async def ab_78(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "18:30-19:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)

    

@dp.message_handler(text="20:30-21:30", state="*")
async def ab_79(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_51.text_box_2.set()

@dp.message_handler(state=Auth_51.text_box_2)
async def ab_80(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "20:30-21:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="22:30-23:30", state="*")
async def ab_81(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_52.text_box_2.set()

@dp.message_handler(state=Auth_52.text_box_2)
async def ab_82(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "22:30-23:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



@dp.message_handler(text="24:30-01:30", state="*")
async def ab_83(message: types.Message, state: FSMContext):
    await message.answer(f"""<b>Comment yozing!</b>""", parse_mode="HTML")
    await Auth_53.text_box_2.set()

@dp.message_handler(state=Auth_53.text_box_2)
async def ab_84(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", "24:30-01:30", f"{data_m.get('text_box_2')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()
        await message.answer(f"<b>Muvaffaqyatli qo'shildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



#UPDATE


class Auth_900(StatesGroup):
    name = State()
    text_box_1 = State()
    text_box_4 = State()


@dp.message_handler(text="✏️ Edit", state="*")
async def on_start_2(message: types.Message, state: FSMContext):
    sql = "SELECT * FROM time_table_2 WHERE user_id ='{}'".format(f"1")
    cursor.execute(sql)
    myresult = cursor.fetchall()
    res = """<b>🔰 Bron qilingan vaqtlar</b>\n\n"""
    for k in myresult:
        res += f"""<b> {k[0]}.🕝 Time: {k[2]}\n\n</b>"""
    await message.answer(res, parse_mode="HTML")
    print("1")
    await message.answer(f"""<b>Avvalgi vaqtni tartib raqamini kiriting! Masalan(7) </b>""", parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
    await Auth_900.name.set()

@dp.message_handler(state=Auth_900.name)
async def name_update(message: types.Message, state: FSMContext):
    name = message.text
    print("abbos")
    if name.isalpha():
        await message.answer(f"<b>Iltimos harf kiritmang!</b>", parse_mode="HTML")
    else:
        print("2")
        await state.update_data(name=name)
        await message.answer("<b>Yangi vaqtni kiriting! Masalan(18:00{}19:00)</b>", parse_mode="HTML")
        await Auth_900.text_box_4.set()
        print("22")

@dp.message_handler(state=Auth_900.text_box_4)
async def name12_update12(message: types.Message, state: FSMContext):
    print("222")
    text_box_4 = message.text.format("-")
    if text_box_4.isalpha():
        await message.answer(f"<b>Iltimos harf kiritmang!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_4=text_box_4)
        await message.answer(f"<b>Yangi Commentni yozing!</b>", parse_mode="HTML")
        await Auth_900.text_box_1.set()

@dp.message_handler(state=Auth_900.text_box_1)
async def text_box_o_update(message: types.Message, state: FSMContext):
    text_box_1 = message.text
    if text_box_1.isdigit():
        await message.answer(f"<b>Iltimos raqam kiritmang!</b>", parse_mode="HTML")
    else:
        print("4")
        await state.update_data(text_box_1=text_box_1)
        db.commit()
        # global data
        data = await state.get_data()
        a = f"{data.get('name')}"
        sql = "DELETE FROM time_table_2 WHERE id = '{}'".format(f"{a}")
        cursor.execute(sql)
        db.commit()
        print("5")
        now = datetime.datetime.now()
        sql = "INSERT INTO time_table_2 (user_id, time, comment, time_now) VALUES (%s, %s, %s, %s)"
        val = (f"1", f"{data.get('text_box_4')}", f"{data.get('text_box_1')}", f"{now}")
        cursor.execute(sql, val)
        db.commit()

        await message.answer("""<b>Muvaffaqiyatli o'zgartirildi</b>""" , parse_mode = 'HTML',reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)




#DELETE

class Auth_100(StatesGroup):
    text_box_2 = State()

@dp.message_handler(text="🗑️ Delete", state="*")
async def on_start_26776(message: types.Message, state: FSMContext):
    sql = "SELECT * FROM time_table_2 WHERE user_id ='{}'".format(f"1")
    cursor.execute(sql)
    myresult = cursor.fetchall()
    res = """<b>🔰 Bron qilingan vaqtlar</b>\n\n"""
    for k in myresult:
        res += f"""<b> {k[0]}.🕝 Time: {k[2]}\n\n</b>"""
    await message.answer(res, parse_mode="HTML")
    await message.answer(f"""<b>O'chirmoqchi bo'lgan vaqtingizni tartib raqamini yozing!</b>""", parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
    await Auth_100.text_box_2.set()

@dp.message_handler(state=Auth_100.text_box_2)
async def name_123(message: types.Message, state: FSMContext):
    text_box_2 = message.text
    if text_box_2.isalpha():
        await message.answer(f"<b>Iltimos harf kiritmang!!</b>", parse_mode="HTML")
    else:
        await state.update_data(text_box_2=text_box_2)
        data_m = await state.get_data()
        a = f"{data_m.get('text_box_2')}"
        sql = "DELETE FROM time_table_2 WHERE id = '{}'".format(f"{a}")
        cursor.execute(sql)
        db.commit()
        await message.answer(f"<b>Muvaffaqiyatli o'chirildi!</b>", parse_mode="HTML", reply_markup=bosh_sahifa_inline_4)
        await state.reset_state(with_data=True)



#TOZALASH


@dp.message_handler(text="❌ Tozalash")
async def menu_tozalash(message: types.Message):
    sql = "DELETE FROM time_table_2 WHERE user_id = '{}'".format(f"1")
    cursor.execute(sql)
    db.commit()
    await message.answer("Malumotlar tozalandi!",parse_mode = 'HTML',reply_markup = bosh_sahifa_inline_4)








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)