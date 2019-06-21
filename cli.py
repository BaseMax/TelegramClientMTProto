import random
from telethon import TelegramClient, events, sync

api_id = 123123123
api_hash = '86a86a86a86a86a86a868a66a88a68a686a868a6'

client = TelegramClient('MaxSession', api_id, api_hash)
client.start()

# print(client.get_me().stringify())

# client.download_profile_photo('me')
# messages = client.get_messages('myfriend')
# messages[0].download_media()

# client.send_message('myfriend', 'Hello! Talking to you from max bot.')
# client.send_file('myfriend', '/root/bot/sample.jpg')

@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def test(event):
	await event.reply('Hey!')

list_hello=[
	"Hello,",
	"Hi.",
	"Hey,",
]
@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def hello(event):
		await event.reply(random.choice(list_hello))

list_how=[
	"Me too, Thank you.",
	"Thank you very much.",
	"Thank you.",
]
@client.on(events.NewMessage(pattern='(?i)how are you|are you good'))
async def how(event):
		await event.reply(random.choice(list_how))

list_bye=[
	"I hope you have a good dream in sleep, Bye.",
	"Good bye.",
	"Bye!",
]
@client.on(events.NewMessage(pattern='(?i)bye|good bye'))
async def bye(event):
		await event.reply(random.choice(list_bye))

client.run_until_disconnected()
