import torch
import random
import os, copy, types, gc, sys
import numpy as np
import time
from pyllamacpp.model import Model

print("lade model")
start_time = time.time()
model = Model(ggml_model='pytorch_model.bin')

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


print("torch.cuda.memory_allocated: %fGB" %
      (torch.cuda.memory_allocated(0)/1024/1024/1024))
print("torch.cuda.memory_reserved: %fGB" %
      (torch.cuda.memory_reserved(0)/1024/1024/1024))
print("torch.cuda.max_memory_reserved: %fGB" %
      (torch.cuda.max_memory_reserved(0)/1024/1024/1024))
end_time = time.time()
print(end_time-start_time)
print("ready")

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
		context = "User:" + prompt + "response:"
		z = len(context)
		print("context lenge is in Tokens - Words:", z/4, z)

		n = 0
		z = 0
		z = len(context)
		n +=z
		text = ""
		output = ""
		start_time = time.time()
		hey = model.generate(context, n_predict=2)
		zh = len(prompt)
		hey = hey[5:]
		hey = hey[zh:]
		hey = hey[10:]
		await channel.send(hey)
		end_time = time.time()
		x = len(us)
		y = len(text)
		print("USER:", "Characters:", x, "Tokens:", x/4, "BOT:", "Characters:", y, "Tokens:", y/4, "Time:", end_time - start_time, "|", "MAX:", n+y+x)
		with open("C://Users/User/Desktop/RWKV/rwkvstic-quant/conversations.txt", "a") as file:
			file.write("User:" + prompt + "\n")
			file.write("Smuggy:" + output + "\n")
			file.close()

client.run(token)
