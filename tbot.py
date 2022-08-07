import os
from aiogram import Dispatcher, executor, types, Bot
import aiogram.utils.markdown as fmt
from dotenv import load_dotenv


load_dotenv()

token = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=token)
dp = Dispatcher(bot)


print('Telegram BOT connected')
print('======================')

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Ready to work! Type /help for help message')


@dp.message_handler(commands='help')
async def help(message: types.Message):
	await message.reply(
		fmt.text(
			fmt.text('Available commands'),
			fmt.text('/showmethemoney - Link to Test Report in Yandex DataLens'),
			fmt.text('/blacksheepwall - Jupyter Notebook file from test task'),
			fmt.text('/whatsmineismine - Link to GitHub repo with this bot'),
			sep='\n'
		), parse_mode="HTML"
	)


@dp.message_handler(commands='blacksheepwall')
async def fa(message: types.Message):
	await bot.send_document(message.chat.id, document=open('data/seek-n-destroy.ipynb', 'rb'))


@dp.message_handler(commands='showmethemoney')
async def start(message: types.Message):
    await message.reply('Here is the link to report: https://datalens.yandex/onbptig6iahef')


@dp.message_handler(commands='whatsmineismine')
async def start(message: types.Message):
    await message.reply('Here is the link to GitHub repo: https://github.com/Real-Vadimych/test_task_bot')

if __name__ == '__main__':
    executor.start_polling(dp)