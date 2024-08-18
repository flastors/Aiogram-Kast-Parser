from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command

from ..routers import user_router as router

from app.utils import get_applicant_list

@router.message(Command('start'))
async def _start(message: Message):
    await message.answer('Hello, I\'m bot')

@router.message(Command('list'))
async def _list(message: Message):
    file = await get_applicant_list()
    await message.answer_document(BufferedInputFile(file, 'list.csv'))
    
@router.message()
async def _echo(message: Message):
    await message.reply(message.text)