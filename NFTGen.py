import requests
import numpy
from PIL import *
from PIL import Image
import os
import imageio
import time

#Store all the files in each directory into arrays
plantTypesArr = os.listdir("../Frame1/PlantTypes");
bodyTypesArr = os.listdir("../Frame1/BodyTypes");
eyeTypes = os.listdir("../Frame1/EyeTypes");
backgroundTypes = os.listdir("../Frame1/BackGroundTypes");
potTypes = os.listdir("../Frame1/PotTypes");

#Create array of arrays for ease of use
list1 = [plantTypesArr,bodyTypesArr,eyeTypes,backgroundTypes,potTypes]

listExists = []

#Function to check if combination already exists
def checkExtists(arr):
	i = 0;
	j = 0;
	flag = False
	print(len(listExists));
	while j < len(listExists):
		while i < len(arr):
			if arr == listExists[j]:
				flag = True
			else:
				flag = False
				break
			i+=1
		j+=1
	return flag

#Function to generate random combinations
def generateCombinations(arr, index):
	combinationList = []
	i = 0;
	while i < len(arr):
		x = numpy.random.choice(arr[i])
		combinationList.append(x)
		i+=1

	if checkExtists(combinationList) == True:
		print("exists: " + str(index))
		generateCombinations(arr, index)
	else:
		listExists.append(combinationList);
	# print(listExists)
	return combinationList
	#print(len(arr[i]))

#Function to create an images and then create a GIF out of it
def createImage(index, x):
	i = 1;
	images = []
	while i <= 2:
		myStr = "../Frame" + str(i) + "/"

		body = Image.open(myStr + "BodyTypes/" + x[1])
		pot = Image.open(myStr + "PotTypes/" + x[4])
		background = Image.open(myStr + "BackGroundTypes/" + x[3]);
		plant = Image.open(myStr + "PlantTypes/" + x[0]);
		eyes = Image.open(myStr + "EyeTypes/" + x[2]);

		pot.paste(plant, (0,0), plant);
		pot.paste(eyes, (0,0), eyes);
		body.paste(pot, (0,0), pot);
		background.paste(body, (0,0), body);

		img = background
		images.append('../Result/Frame' + str(i) + '/Result' + str(index) + '.png')
		img.save('../Result/Frame' + str(i) + '/Result' + str(index) + '.png', 'PNG')

		i+=1
	images = [imageio.imread(file) for file in images]
	imageio.mimwrite('GifResult/Result' + str(index) +'.gif', images, fps=1, duration=0.2)

def craeteNFT(amount):
	i = 0;
	while i < amount:
		x = generateCombinations(list1, i);
		print("Success..." + str(i));
		createImage(i,x);
		i+=1

craeteNFT(180)
