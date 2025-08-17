#import pygame 
import pygame

#inicialize the library
pygame.init()

#inicialize mix
pygame.mixer.init()

#Loading archive MP3
pygame.mixer.music.load(r"Flog-atumalaca-_.mp3")

#Play music
pygame.mixer.music.play()

#Keep the application running while the music is playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

#Endly Pygame
pygame.quit()


