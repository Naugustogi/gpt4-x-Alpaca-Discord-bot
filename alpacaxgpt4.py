import torch
import random
import os, copy, types, gc, sys
import numpy as np
import time
from pyllamacpp.model import Model

print("lade model")
start_time = time.time()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("start discord package")
import ast
from difflib import SequenceMatcher
from discord.ext import commands
import time 
import re
import discord
import io

token = "" #smuggy
intents = discord.Intents.default() #all
client = discord.Client(intents=intents)
print("apply context")
end_time = time.time()
print(end_time-start_time)
print("ready")

with open("C:/Users/User/Desktop/text generation webui/llama + gpt4all Smuggy/convrn.txt", "w") as file:
	pass
	file.close()
with open("C:/Users/User/Desktop/text generation webui/llama + gpt4all Smuggy/convrn.txt", "a") as file:
	file.write("You are an ai system capable of helping the user with each demand." + "\n")
	file.write("User:" + "Hello how are you doing?" + "\n")
	file.write("Smuggy:" + "I'm good. How can i help you?" + "\n")
	file.close()
@client.event
async def on_message(message):
	print("def loaded")
	if message.author == client.user:
		return
		

#------------------------------------------------
	if  client.user.mentioned_in(message):

		prompt = message.content
		prompt = prompt[23:]
		channel = message.channel

		w = len(prompt)/4
		us = prompt
		print("prompt:", w)
		if(w<1):
			await channel.send(f"Context length is to small. It's: {w}")
			return
		await channel.trigger_typing()
		global output
		global text
		global context
		global n
		global z
		global new_text_callback
		new_text_callback = ""
		with open("C:/Users/User/Desktop/text generation webui/llama + gpt4all Smuggy/convrn.txt", "r") as file:
			context = file.read()
			file.close()
		
		
		context2 = (f"\n User: + {prompt} \n + Smuggy:")
		context = context + context2
		
		z = len(context)
		print("context lenge is in Tokens - Words:", z/4, z)

		n = 0
		z = 0
		z = len(context)
		n +=z
		text = ""
		output = ""
		start_time = time.time()
		model = Model(ggml_model='gpt4-x-alpaca-13b-native-ggml-model-q4_0.bin')
		hey = model.generate(context, n_predict=100)
		zh = len(context)
		zp = len(prompt)
		hey = hey[zh:]
		hey = hey[5:]
		hey = hey[zp:]
		await channel.send(hey)
		end_time = time.time()
		x = len(us)
		y = len(text)
		print("USER:", "Characters:", x, "Tokens:", x/4, "BOT:", "Characters:", y, "Tokens:", y/4, "Time:", end_time - start_time, "|", "MAX:", n+y+x)
		with open("C:/Users/User/Desktop/text generation webui/llama + gpt4all Smuggy/conversations.txt", "a") as file:
			file.write("User:" + prompt + "\n")
			file.write("Smuggy:" + hey + "\n")
			file.close()
		with open("C:/Users/User/Desktop/text generation webui/llama + gpt4all Smuggy/convrn.txt", "a") as file:
			file.write("User:" + prompt + "\n")
			file.write("Smuggy:" + hey + "\n")
			file.close()

client.run(token)
