import discord
import random
import requests
import keep_alive
import json
client = discord.Client()
api_key = 'youtube v3 api key'
channel_id = 'click on a channel and look at the url to figure out its id'
base_layer_vid_url = 'https://www.youtube.com/watch?v='
base_layer_api_search_url = 'https://www.googleapis.com/youtube/v3/search?'
first_url = base_layer_api_search_url + 'key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1'
url = first_url
@client.event
async def on_message(message):
                if message.content == "/word":
                        my_file = open("word_list.txt", "r")
                        words = my_file.readlines()

                        random_thing = (random.randint(0, 160))
                        a = random_thing + 2

                        word = words[random_thing]
                        if (random_thing % 2 == 0):

                                bog = (words[random_thing + 1])
                                xyz = (word)
                                await message.channel.send(xyz + bog)

                        else:
                                bog = (words[random_thing - 1])
                                xyz = (word)

                                await message.channel.send(bog + xyz)

                else:
                        if message.content == "/fact":
                                with open('facts.txt') as f:
                                        g = f.readlines()
                                await message.channel.send(random.choice(g))



                        else:

                                        if message.content == "/member_count":
                                                id = client.get_guild('find your discord server or channel id')
                                                await message.channel.send(f"""{id.member_count}""")
                                        else:
                                                if message.content == "/latest":
                                                        inp = requests.get(url)

                                                        resp = json.loads(inp.text)

                                                        for i in resp['items']:
                                                                if i['id']['kind'] == "youtube#video":
                                                                        await message.channel.send(
                                                                                (base_layer_vid_url + i['id']['videoId']))

keep_alive.keep_alive()

client.run('get discord token to run')




































