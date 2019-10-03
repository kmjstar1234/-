import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("간호사")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):
    if message.content.startswith("ㅎㅇ"):
        await message.channel.send("응 아니야")
    if message.content.startswith("양재민은"):
        await message.channel.send("그저 병신")
    if message.content.startswith("구명재는"):
        await message.channel.send("그저 이 서버의 조물주")
    if message.content.startswith("유재영은"):
        await message.channel.send("그저 천재라 우기는 병신")
    if message.content.startswith("김건우는"):
        await message.channel.send("그저 좆밥")
    if message.content.startswith("안현우는"):
        await message.channel.send("그저 잘난척쟁이")
    if message.content.startswith("김호재는"):
        await message.channel.send("SM play")
    if message.content.startswith("장석호는"):
        await message.channel.send("변태 색기")
    if message.content.startswith("김호재는"):
        await message.channel.send("이현전은")
    if message.content.startswith("박진현은"):
        await message.channel.send("아프리카 돼지열병 걸린 븅신")








client.run("NjI5MTM4NTUxMDczNjY5MTMx.XZWtnQ.fIlNZhVwytaHqYLgfMoAvp6rgHw")
