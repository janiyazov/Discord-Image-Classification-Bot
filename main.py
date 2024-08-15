import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/',
                   intents=intents,
                   help_command=None)

bot.event
async def on_ready():
    print(f'Бот {bot.user} готов к работе')

bot.command()
async def photo(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.filename.endswith(''.jpg') or \
            attachment.filename.endswith('.jpeg') or \
            attachment.filename.endswith('.png'):
                image_path = f'./images/{attachment.filename}'
                await attachment.save(image_path)
                temp_msg = await ctx.send('Идет обработка изображения ')
                class_name, score = get_class(image_path,
                                              'gtm_model/keras_model.h5',
                                              'gtm_model/labels.txt')
                await temp_msg.delete()
                await ctx.send(f'С вероятностью {score}% на фото {class_name.lower()}')
                os.remowe(image_path)
            else:
                await ctx.send('Файл должен иметь расширение jpg / .jpeg / .png')
                return
    else:
        await ctx.send('Кажется, ты забыл загрузить фото ;с')

bot.run(DISCORD_TOKEN)
