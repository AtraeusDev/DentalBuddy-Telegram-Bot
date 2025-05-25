import asyncio
import random
from aiogram import Router
from aiogram.filters import CommandStart 
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.enums import ChatAction

from app.states import ConsultationStates
from app.generators import text


router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.bot.send_chat_action(chat_id=message.from_user.id, 
                                       action=ChatAction.TYPING)
    await asyncio.sleep(random.uniform(2, 4))
    await message.answer('Здравствуйте! Меня зовут Алексей, я ассистент стоматологической клиники "Улыбка". '
                         'Я помогу вам записаться на процедуру и отвечу на вопросы, что вас беспокоит?')
    
    await state.set_state(ConsultationStates.waiting_symptoms)

@router.message(ConsultationStates.waiting_symptoms)
async def handle_symptoms(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_message = message.text
    await state.update_data(symptoms=user_message)

    response = await text(user_id, user_message)
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                       action=ChatAction.TYPING)
    await asyncio.sleep(random.uniform(2, 4))
    await message.answer(response)


