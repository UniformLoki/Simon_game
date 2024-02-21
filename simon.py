import pinworkslabs.RPi as GPIO
from random import choice
from time import sleep
import pygame
import pygame.mixer import Sound
import os

pygame.init()

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)


class Button:
    def __init__(self,switch:int,led:int,sound:str,color:str):
        


class Simon:
    WELCOME_MESSAGE = "Welcome to Simon! press ctcl + c"
    
    BUTTONS = [ Button(switch=20,led=6,sound=os.path.join("sounds","one.wav"),color="red"),
               Button(switch=16,led=13,sound=os.path.join("sounds","two.wav"),color="blue"),
               Button(switch=12,led=19,sound=os.path.join("sounds","three.wav"),color="yellow"),
               Button(switch=26,led=21,sound=os.path.join("sounds","four.wav"),color="green")]

    def __init__(self,debug=True):
        self.debug = debug
        self.sequence:list[Button] = []
        
    def debug_out(self, *args):
        if self.debug:
            print(*args)
            
            
    def blink_all_buttons(self):
        leds = []
        for button in Simon.BUTTONS:
            leds.append(button.led)
        GPIO.output(leds,True)
        sleep(.5)
        GPIO.output(leds,False)
        sleep(.5)
        
        #alternative
        #for button in Simon.BUTTONS:
        #    button.turn_light_on()
        #    sleep(.5)
        #    button.turn_light_off()
        #    sleep(.5)
    
    def add_to_sequence(self):
        dandom_button = choice(Simon.BUTTONS)
        self.sequence.append(random_button)
    
    
    def lose(self):
        for _ in range(4):
            self.blink_all_buttons()
        GPIO.cleanup()
        exit()
    
    def playback(self):
        for button in self.sequence:
            button.respond()
            
            
    def wait_for_press():
        while True:
            for button in Simon.BUTTONS:
                if button.is_pressed():
                    self.debug_out(button.color)
                    button.respond()
                    return button #kills the while True and tells what button was pressed
    
    def check_input(self,pressed_button,correct_button):
        if pressed_button.switch != correct_button.button:
            self.lose()
    
    def run(self):
        print(Simon.WELCOME_MESSAGE)
        self.add_to_sequence()
        self.add_to_sequence()
        
        try:
            while True:
                self.add_to_sequence()
                self.playback()
                self.debug_out(*self.sequence)
                for button in self.sequence:
                    pressed_button = self.wait_for_press()
                    self.check_input(pressed_button,button)
                
    
        except KeyboardInterrupt:
            