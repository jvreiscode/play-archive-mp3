import pygame

# Inicializa o Pygame
pygame.init()

# Inicializa o mixer
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load(r"C:\Users\jvsoa\OneDrive\Documents\Programação\Faculdade\arquivosPy\Sapo-atumalaca-_.mp3")

# Toca a música
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Encerra o Pygame
pygame.quit()
