import discord, random
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        hod_komp = random.choice(('камень', 'ножницы', 'бумага'))
        if message.author == self.user:
            return


        if message.content == '1.1':
            if hod_komp == 'камень':
                await message.channel.send('1')
            if hod_komp == 'ножницы':
                await message.channel.send('2')
            if hod_komp == 'бумага':
                await message.channel.send('3')

        if message.content == '1.2':
            await message.channel.send('<:Ernest_salute:830729959764393984> ')

        if message.content == 'камень':
            if hod_komp == 'камень':
                await message.channel.send('Камень! Ничья, чел')
            if hod_komp == 'ножницы':
                await message.channel.send('Ножницы, я проиграль(')
            if hod_komp == 'бумага':
                await message.channel.send('Бумага! Ха-ха, ничтожество')
        elif message.content == 'ножницы':
            if hod_komp == 'ножницы':
                await message.channel.send('Ножницы! Ничья, чел')
            if hod_komp == 'бумага':
                await message.channel.send('Бумага, я проиграль(')
            if hod_komp == 'камень':
                await message.channel.send('Камень! Ха-ха, ничтожество')
        elif message.content == 'бумага':
            if hod_komp == 'бумага':
                await message.channel.send('Бумага! Ничья, чел')
            if hod_komp == 'камень':
                await message.channel.send('Камень, я проиграль(')
            if hod_komp == 'ножницы':
                await message.channel.send('Ножницы! Ха-ха, ничтожество')
        else:
            return



client = MyClient()
client.run('NzgzNTg1MjkwMDY5MjEzMjY0.X8c4qw.bz6z-RjEnI445KImUC0rfrYxRCQ')
