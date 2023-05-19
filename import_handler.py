import pygame, math, sys, Graph_and_Nodes, threading
from pygame.locals import *
import pygame_textinput
from pygame_textinput import *
pygame.init()
screen_size = screen_width, screen_height = 1280, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Dijkstra\'s algorithm simulator")
clock = pygame.time.Clock()
counter = 0

black = (15, 15, 15)
red = (255, 0, 0)
white = (255, 255, 255)
gray = (145, 145, 145)
light_green = (144, 238, 144)