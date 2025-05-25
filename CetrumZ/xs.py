import pygame
import pyautogui
import random
import subprocess
from PIL import Image

subprocess.run(["python", "dcs.py"])

pygame.init()
screen_info = pygame.display.Info()
screen_w, screen_h = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)
pygame.display.set_caption("VeryVirus CRDS")

font = pygame.font.SysFont("Courier New", 64, bold=True)
clock = pygame.time.Clock()

def get_screenshot_surface():
    screenshot = pyautogui.screenshot()
    img = screenshot.convert("RGB").resize((screen_w, screen_h))
    data = img.tobytes()
    return pygame.image.fromstring(data, img.size, "RGB")

def draw_stop_button():
    btn_color = (255, 0, 0)
    btn_rect = pygame.Rect(screen_w - 220, screen_h - 80, 200, 60)
    pygame.draw.rect(screen, btn_color, btn_rect)
    label = font.render("STOP", True, (255, 255, 255))
    screen.blit(label, (btn_rect.x + 20, btn_rect.y + 5))
    return btn_rect

running = True
color_flash = (0, 0, 0)

while running:
    color_flash = (
        random.randint(20, 255),
        random.randint(20, 255),
        random.randint(20, 255)
    )
    screen.fill(color_flash)

    screenshot = get_screenshot_surface()
    screen.blit(screenshot, (0, 0))

    for _ in range(20):
        x = random.randint(0, screen_w - 100)
        y = random.randint(0, screen_h - 100)
        w = random.randint(50, 200)
        h = random.randint(30, 150)
        offset_x = random.randint(-50, 50)
        offset_y = random.randint(-50, 50)
        try:
            region = screenshot.subsurface((x, y, w, h)).copy()
            screen.blit(region, (x + offset_x, y + offset_y))
        except:
            pass

    text_color = (
        random.randint(100, 255),
        random.randint(100, 255),
        random.randint(100, 255)
    )
    virus_text = font.render("VeryVirus CRDS", True, text_color)
    screen.blit(virus_text, (screen_w // 2 - 300, screen_h // 2 - 50))

    stop_button = draw_stop_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if stop_button.collidepoint(event.pos):
                running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
