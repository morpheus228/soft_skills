import asyncio
from aiogram import Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Bot, Router
from aiogram.fsm.state import State, StatesGroup

from utils.message_template import MessageTemplate
import logging
import httpx


logging.basicConfig(level=logging.INFO)


router = Router()


class States(StatesGroup):
    start = State()
    color = State()
    relax = State()
    happy = State()
    angry = State()
    bad_people = State()
    can_not_forgive = State()
    music = State()
    weak_skill = State()
    sphere = State()
    result = State()



@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    text, reply_markup = MessageTemplate.from_json('start').render()
    await message.answer(text, reply_markup=reply_markup)
    await state.set_state(States.start)


@router.message(States.start)
async def start(message: Message, state: FSMContext):
    if message.text != "Начать":
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        text, reply_markup = MessageTemplate.from_json('color').render()
        await message.answer(text, reply_markup=reply_markup)
        await state.set_state(States.color)


@router.message(States.color)
async def color(message: Message, state: FSMContext):
    if message.text not in ["Синий", "Красный", "Чёрный", "Белый", "Зелёный"]:
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        await state.update_data(color=message.text)
        text, reply_markup = MessageTemplate.from_json('relax').render()
        await message.answer(text, reply_markup=reply_markup)
        await state.set_state(States.relax)


@router.message(States.relax)
async def relax(message: Message, state: FSMContext):
    if message.text not in ["Общение с друзьями", "Чтение книг (Или иной способ убежать от реальности)", "Нагрузка на своё тело/выплёскивание эмоций в физическую силу", "Сон"]:
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        await state.update_data(relax=message.text)
        text, reply_markup = MessageTemplate.from_json('happy').render()
        await message.answer(text, reply_markup=reply_markup)
        await state.set_state(States.happy)


@router.message(States.happy)
async def happy(message: Message, state: FSMContext):
    if message.text not in ["Новое знакомство с подходящим по характеру к тебе человеком", "Получение подарка от кого-либо", "Приятные слова от близкого человека", "Радость твоих друзей", "Прогресс в тренировках в чём-либо", "Месть кому-либо"]:
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        await state.update_data(happy=message.text)
        text, reply_markup = MessageTemplate.from_json('angry').render()
        await message.answer(text, reply_markup=reply_markup)
        await state.set_state(States.angry)


@router.message(States.angry)
async def angry(message: Message, state: FSMContext):
    if message.text not in ["Проигрыш в чём-либо", "Несоблюдение/неработоспособность плана", "Выход из зоны комфорта", "Радость других людей"]:
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        await state.update_data(angry=message.text)
        text, reply_markup = MessageTemplate.from_json('bad_people').render()
        await message.answer(text, reply_markup=reply_markup)
        await state.set_state(States.bad_people)


@router.message(States.bad_people)
async def bad_people(message: Message, state: FSMContext):
    if message.text not in ["Жестокость", "Лживость", "Лицемерие", "Наглость", "Мстительность"]:
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        await state.update_data(bad_people=message.text)
        text, reply_markup = MessageTemplate.from_json('can_not_forgive').render()
        await message.answer(text, reply_markup=reply_markup)
        await state.set_state(States.can_not_forgive)


@router.message(States.can_not_forgive)
async def can_not_forgive(message: Message, state: FSMContext):
    if message.text not in ["С предательством тебя твоим же другом", "С потерей очень ценных для тебя материальных ценностей", "С успехом человека добившегося своего результата благодаря краже твоей идеи", "В своей ненадобности обществу", "Ничего не сломит мою волю!"]:
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        await state.update_data(can_not_forgive=message.text)
        text, reply_markup = MessageTemplate.from_json('music').render()
        await message.answer(text, reply_markup=reply_markup)
        await state.set_state(States.music)


@router.message(States.music)
async def music(message: Message, state: FSMContext):
    if message.text not in ["Слушаю только хиты", "Предпочитаю один стиль", "Слушаю все подряд", "Другое"]:
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        await state.update_data(music=message.text)
        text, reply_markup = MessageTemplate.from_json('weak_skill').render()
        await message.answer(text, reply_markup=reply_markup)
        await state.set_state(States.weak_skill)


@router.message(States.weak_skill)
async def weak_skill(message: Message, state: FSMContext):
    if message.text not in ["Критическое мышление", "Эмоциональный интеллект", "Коммуникабельность", "Креативность", "Управление временем", "Лидерство"]:
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        await state.update_data(weak_skill=message.text)
        text, reply_markup = MessageTemplate.from_json('sphere').render()
        await message.answer(text, reply_markup=reply_markup)
        await state.set_state(States.sphere)

    

@router.message(States.sphere)
async def sphere(message: Message, state: FSMContext):
    if message.text not in ["Работа", "Учеба", "Личная жизнь", "Все варианты"]:
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        await state.update_data(sphere=message.text)
        text, reply_markup = MessageTemplate.from_json('result').render()
        await message.answer(text, reply_markup=reply_markup)
        await state.set_state(States.result)


@router.message(States.result)
async def result(message: Message, state: FSMContext):
    if message.text not in ["Небольших изменений в навыках", "Кардинальной смены привычек", "Никакого"]:
        text, reply_markup = MessageTemplate.from_json('error').render()
        await message.answer(text, reply_markup=reply_markup)
    
    else:
        await state.update_data(result=message.text)
        data = await state.get_data()

        async with httpx.AsyncClient() as client:
            response = await client.post('http://127.0.0.1/predict', json=data)

        try:
            text, reply_markup = MessageTemplate.from_json('answer').render(course=response.json()['result'])
            await message.answer(text, reply_markup=ReplyKeyboardRemove())
        except:
            text, reply_markup = MessageTemplate.from_json('bad_request').render()
            await message.answer(text, reply_markup=ReplyKeyboardRemove())
        
        await state.clear()


async def main():
    bot = Bot("6653187081:AAGgm7Fu23kfi750_z_sS_0P9_JXTTGXjlQ", parse_mode='HTML')
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
