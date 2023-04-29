import torch
import random
import os, copy, types, gc, sys
import numpy as np
import time
#from pyllamacpp.model import Model
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
token = "" #sage
intents = discord.Intents.default() #all
client = discord.Client(intents=intents)
end_time = time.time()
model = Model(ggml_model='gpt4-x-alpaca-13b-native-ggml-model-q4_0.bin', n_ctx=2048, f16_kv=1) #, use_mlock=True logits_all=0
print("Model loading time: ", end_time-start_time)
print("apply context")
with open("sage.txt", "w") as file:
	pass
	file.close()
with open("sage.txt", "a") as file:
	file.write("You are Sage, a highly advanced intelligent AI System."+"\n")
	file.write("Enju:How are you doing?" + "\n)
	file.write("Sage:I'm good! Do you have any other questions??" + "\n")
	file.close()

print("Ready")
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
		print("User/Enju: ", prompt)
		with open("sage.txt", "a") as file:
			file.write("Enju:" + prompt + "\n")
			file.close()
		w = len(prompt)/4
		us = prompt
		print("prompt:", w)
		if(w<1):
			await channel.send(f"Context length is to small. It's: {w}")
			return
		#await channel.trigger_typing()
		global text
		global context
		global n
		global z
		global m
		global output
		output = ""
		m = 1
		global new_text_callback
		new_text_callback = ""
		if("mode1" in prompt):
			m = 1
			await channel.send("I have changed my mode to 1")
			return
		if("mode2" in prompt):
			m = 2
			await channel.send("I have changed my mode to 2")
			return
		if(m==1):
			with open("sage.txt", "r") as file:
				context = file.read()
				file.close()
				context2 = ("\n" + "Sage:")
				context = context + context2
		if(m==2):
			context = ("Enju:" + prompt + "\n")
			
			
		z = len(context)
		print("context lenge is in Tokens - Words:", z/4, z)
		global hey
		n = 0
		z = 0
		z = len(context)
		n +=z
		text = ""
		start_time = time.time()
		hey = ""
		#hey = model.generate(context, n_predict=1000, temp=0.01, n_threads = 20) #n_batch = 1 ,#Sage 19175 #Enju 5141021
		for token in model.generate(context, n_predict=1000, n_threads = 12, top_k = 40, top_p = 0.95, temp=0.01, repeat_penalty = 1.3): # n_predict = none top_p = 1
			hey = hey + token
			print(hey)
		print(hey)
		cont = len(context)
		#hey = hey[cont:]
		#hey = hey[1:]
		print("Sage: ", hey)
		await channel.send(hey)
		end_time = time.time()
		x = len(us)
		y = len(text)
		print("USER:", "Characters:", x, "Tokens:", x/4, "BOT:", "Characters:", y, "Tokens:", y/4, "Time:", end_time - start_time, "|", "MAX:", n+y+x)
		with open("sageconv.txt", "a") as file:
			file.write("Enju:" + prompt + "\n")
			file.write("Sage:" + hey + "\n")
			file.close()
		with open("sage.txt", "a") as file:
			file.write("Sage:" + hey + "\n")
			file.close()

client.run(token)
