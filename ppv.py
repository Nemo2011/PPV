# Pygame Picture Viewer
# V1.0
import sys
from tkinter import filedialog, messagebox
import pygame
location = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
if not location:
    sys.exit()
try:
    sur = pygame.image.load(location)
except:
    sys.exit()
scr = pygame.display.set_mode((sur.get_rect().width, sur.get_rect().height))
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            rgb = scr.get_at(pos)
            messagebox.showinfo(str(rgb), str(rgb))
    scr.blit(sur, sur.get_rect())
    pygame.display.flip()
