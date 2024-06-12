# Pygame Template

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1024, 768), 0, 32)
pygame.display.set_caption("Spy Hangman")
FPSspeed = pygame.time.Clock()
imgBGImage = 'bank.jpg'
BG = pygame.image.load(imgBGImage).convert()
pygame.mixer.pre_init(44100, -16, 2, 2048)

# classes go here

class Logo:
	def __init__(self):
		self.BlackInk = (0, 0, 0)
		self.BlueInk = (0, 90, 255)
		self.x = 184
		self.y = 100
		self.size = 100
		self.font = pygame.font.SysFont('consolas', 120)
		self.logo = self.font.render("SPY HANGMAN", True, self.BlueInk)
		
	def draw(self):
		pygame.draw.rect(screen, self.BlackInk, (self.x, self.y, self.size * 7.25, self.size), 0)
		screen.blit(self.logo, (self.x, self.y))
		
class GeneralScreen:
	def __init__(self, image, width, height):
		self.image = pygame.image.load(image)
		self.width = width
		self.height = height
		
class MainGameScreen:
	def __init__(self, image, width, height):
		self.screen = pygame.display.set_mode((width, height))
		self.image = pygame.image.load(image)
		self.width = width
		self.height = height

class SplashScreen:
	def __init__(self, image, width, height):
		self.screen = pygame.display.set_mode((width, height))
		self.image = pygame.image.load(image)
		self.width = width
		self.height = height
		# self.sound = pygame.mixer.Sound('detective-15646.mp3')
		
	def run(self):
		self.screen.blit(self.image, (0, 0))
		self.sound.play()
		pygame.time.wait(5000) # 5000 = 5 seconds
	
	def close(self):
		pygame.quit()
		sys.exit()
		
class PlayButton: 
	def __init__ (self):
		self.LightGreenInk = (0, 255, 0)
		self.DarkGreenInk = (0, 100, 0)
		self.WhiteInk = (255, 255, 255)
		self.BlackInk = (0, 0, 0)
		self.size = 50
		self.x = 450
		self.y = 500
		self.font = pygame.font.SysFont('arial', 40)
		self.mouse = False
		self.show = True

	def draw(self):
		if self.show == True:
			if self.mouse == True:
				pygame.draw.rect(screen, self.DarkGreenInk, (self.x, self.y, self.size * 3, self.size), 0)
				self.letter = self.font.render("Play", True, self.WhiteInk)
			else:
				pygame.draw.rect(screen, self.LightGreenInk, (self.x, self.y, self.size * 3, self.size), 0)
				self.letter = self.font.render("Play", True, self.BlackInk)
		
		screen.blit(self.letter, (self.x + 45, self.y))

	def mouseover(self):
		x, y = pygame.mouse.get_pos()
		if self.x <= x < self.x + self.size and self.y <= y < self.y + self.size:
			self.mouse = True
		else:
			self.mouse = False
			
	def click(self, events):
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos()
				if self.x <= x < self.x + self.size and self.y <= y < self.y + self.size:
						print(self.name)
						return self.name
		return None

# class InstructionsScreen():
		
class DifficultyScreen:
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.Font(None, 36)
		self.buttons = {
			"easy": pygame.Rect(100, 75, 100, 50),
			"medium": pygame.Rect(250, 75, 100, 50),
			"hard": pygame.Rect(400, 75, 100, 50)
		}
	
	def draw(self):
		for text, rect in self.buttons.items():
			pygame.draw.rect(self.screen, (255, 0, 0), rect)
			label = self.font.render(text, True, (255, 255, 255))
			label_rect = label.get_rect(center=rect.center)
			self.screen.blit(label, label_rect)
			
	def difficulty(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = event.pos
					for difficulty, rect in self.buttons.items():
						if rect.collidepoint(mouse_pos):
							return difficulty
				self.screen.fill((0, 0, 0))
				self.draw()
				pygame.display.flip()
				
'''
class button:
	def __init__(self, text, x, y, w, h):
		self.rect = pygame.Rect(x, y, w, h)
		self.text = text		
		self.mouse = False
		self.clicked = False
		self.font = pygame.font.SysFont('arial', int(h))

	def draw(self):
		
		# Deals with mousover display
		if self.mouse == True:			
			pygame.draw.rect(screen, (255, 255, 255), self.rect, 0)
			self.letter = self.font.render(self.text, True, (0, 0, 0))
			screen.blit(self.letter, (self.rect.x +4, self.rect.y-2))
		else:
			pygame.draw.rect(screen, (255,255,255), self.rect, 1)
			self.letter = self.font.render(self.text, True, (0, 0, 0))
			screen.blit(self.letter, (self.rect.x +4, self.rect.y-2))
		
		# Deals with click and returned values
		pos = pygame.mouse.get_pos()
		letterclicked = None
		if self.rect.collidepoint(pos):
			self.mouse = True
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False
		else:
			self.mouse = False
		return letterclicked
		
PlayButton = button('Play', 30, 175, 25, 25)
'''

class KeyboardButton:
	def __init__(self, letter, position):
		self.WhiteInk = (255, 255, 255)
		self.BlackInk = (0, 0, 0)
		self.size = 25
		self.name = letter
		if self.name >= 'a' and self.name <= 'g':
			self.x = 112 + position * 25
			self.y = 75
		elif self.name >= 'h' and self.name <= 'n':
			self.x = -63 + position * 25
			self.y = 100
		elif self.name >= 'i' and self.name <= 'u':
			self.x = -238 + position * 25
			self.y = 125
		elif self.name >= 'v':
			self.x = -388 + position * 25
			self.y = 150
			
		self.font = pygame.font.SysFont('arial', 20)
		self.mouse = False
		self.show = True
		
	def draw(self):
		if self.show == True:
			if self.mouse == True:
				pygame.draw.rect(screen, self.WhiteInk, (self.x, self.y, self.size, self.size), 0)
				self.letter = self.font.render(self.name, True, self.BlackInk)
			else:
				pygame.draw.rect(screen, self.BlackInk, (self.x, self.y, self.size, self.size), 0)
				self.letter = self.font.render(self.name, True, self.WhiteInk)
				
		screen.blit(self.letter, (self.x + 8, self.y))
		
	def mouseover(self):
		x, y = pygame.mouse.get_pos()
		if self.x <= x < self.x + self.size and self.y <= y < self.y + self.size:
			self.mouse = True
		else:
			self.mouse = False
			
	def click(self, events):
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos()
				if self.x <= x < self.x + self.size and self.y <= y < self.y + self.size:
						print(self.name)
						return self.name
		return None

Alphabet = "abcdefghijklmnopqrstuvwxyz"
Keyboard = [KeyboardButton(letter, index) for index, letter in enumerate(Alphabet)]

class Player():
	def __init__(self):
		self.image = pygame.image.load('spy.png').convert_alpha()
		self.x = 650
		self.y = 300
		
	def draw(self):
		screen.blit(self.image, (self.x, self.y))
		
class Word:
	def __init__(self, level):
		# Pre: this is the initializer function to create the instance
		# Post: new word with the given size parameters
		Words = open("Dictionary_Pygame.txt").read().split("\n")
		self.SecretWord = random.choice(Words)
		
		if (level=='E'):
			iLow = 10
			iHigh = 100
		elif (level=='M'):
			iLow = 7
			iHigh = 9
		elif (level=='H'):
			iLow = 3
			iHigh = 6
			
		while (len(self.SecretWord) < iLow or len(self.SecretWord) > iHigh):
			self.SecretWord = random.choice(Words)
		
		self.x = 100
		self.y = 450
		self.LettersGuessed = ''
		self.Reveal = ''
		self.letter = ''
		self.rect = (self.x, self.y, len(self.SecretWord)*30, 30)
		self.font = pygame.font.SysFont('arial', 30)
		
	def RevealWord(self):
		self.Reveal = '' # Null
		for char in self.SecretWord:
			if char in self.LettersGuessed:
				self.Reveal += char
			else:
				self.Reveal += '_' # Unlike the text-based version, we are not adding a space
		return self.Reveal # pi__a
		
	def draw(self):
		# Pre:
		# Post:
		position = 0
		for char in self.Reveal: # p i _ _ a
			position += 1
			if char == '_':
				pygame.draw.line(screen, (255, 255, 255), 
				(self.x + position * 30, self.y), 
				(self.x + position * 30 + 15, self.y), 2)
			else:
				self.letter = self.font.render(char, True, (255, 255, 255))
				screen.blit(self.letter, (self.x + position * 30 + 2, self.y - 30))

class Board():
	def __init__(self):
		self.x = 300
		self.y = 300
		self.image = pygame.image.load('frame.png').convert()

	def draw(self):
		screen.blit(self.image, (self.x, self.y))

class Criminal():
	def __init__(self):
		self.image = []
		self.show = False
		self.x = 300
		self.y = 150
		for iCounter in range(0,8):
			self.image.append[pygame.image.load('criminal_costume_'+str(iCounter)+'.png')]
		for iCounter in range(0,8):
			self.image[iCounter] = pygame.transform.scale(self.image[iCounter], (320, 240))
	
	def draw(self, errors):
		screen.blit(self.image[errors], (self.x, self.y))

class WinScreen():
	def __init__(self):
		self.image = pygame.image.load('win_screen.jpg').convert()

class LossScreen():
	def __init__(self):
		self.image = pygame.image.load('loss_screen.jpg').convert()
		
# Main loop
RunGame = True
while RunGame == True:
		#	0-255,	0-255,	0-255
		#	Red		green	blue
		screen.fill((255, 255, 255))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				RunGame = False
				pygame.quit()
				sys.exit()
			# add other events here

# Update stuff

# Draw screen stuff here
		Logo.draw(Logo())
		# SplashScreen.run(SplashScreen(imgBGImage, 1024, 768))
		PlayButton.draw(PlayButton())
		PlayButton.mouseover(PlayButton())
		pygame.display.update()
