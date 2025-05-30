import pygame
import random
import time

pygame.init()
# pygame.mixer.init()
# eat_sound = pygame.mixer.Sound("eat.wav")  

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")

size1 = 50  # Kích thước ban đầu của nhân vật 1
img1_raw = pygame.image.load("gameArt.png")
img1 = pygame.transform.scale(img1_raw, (size1, size1))

img2 = pygame.image.load("apple.png")
img2 = pygame.transform.scale(img2, (30, 30))



img3 = pygame.image.load("boom.png")
img3 = pygame.transform.scale(img3, (100, 100))


x1, y1 = 0, 0
x2, y2 = 100, 100
x3, y3 = 200, 200


FPS = 60
clock = pygame.time.Clock()

visible2 = True
hide_time = 0

score = 0  # Thêm biến điểm số
font = pygame.font.SysFont(None, 36)  # Font để hiển thị điểm

def check_collision(x1, y1, x2, y2, size1=50, size2=30):
    rect1 = pygame.Rect(x1, y1, size1, size1)
    rect2 = pygame.Rect(x2, y2, size2, size2)
    return rect1.colliderect(rect2)

def check_win(score):
    if score >= 7:
        win_font = pygame.font.SysFont(None, 80)
        win_text = win_font.render("YOU WON", True, (0, 0, 255))
        WINDOW.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Hiển thị 2 giây
        return True
    return False

def check_lose(x1, y1, x3, y3, size1=50, size3=100):
    rect1 = pygame.Rect(x1, y1, size1, size1)
    rect3 = pygame.Rect(x3, y3, size3, size3)
    if rect1.colliderect(rect3):
        lose_font = pygame.font.SysFont(None, 80)
        lose_text = lose_font.render("LOSE", True, (255, 0, 0))
        WINDOW.blit(lose_text, (WIDTH // 2 - lose_text.get_width() // 2, HEIGHT // 2 - lose_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Hiển thị 2 giây
        return True
    return False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Điều khiển nhân vật 1
    dx1, dy1 = 0, 0
    if keys[pygame.K_LEFT]:
        dx1 = -5
    if keys[pygame.K_RIGHT]:
        dx1 = 5
    if keys[pygame.K_UP]:
        dy1 = -5
    if keys[pygame.K_DOWN]:
        dy1 = 5
    x1 = max(0, min(WIDTH - size1, x1 + dx1))
    y1 = max(0, min(HEIGHT - size1, y1 + dy1))


    # Điều khiển nhân vật 3
    dx3, dy3 = 0, 0
    if keys[pygame.K_a]:
        dx3 = -5
    if keys[pygame.K_d]:
        dx3 = 5
    if keys[pygame.K_w]:
        dy3 = -5
    if keys[pygame.K_s]:
        dy3 = 5
    x3 = max(0, min(WIDTH - 70, x3 + dx3))
    y3 = max(0, min(HEIGHT - 70, y3 + dy3))

    # Xử lý va chạm với quả táo
    if visible2:
        if check_collision(x1, y1, x2, y2, size1, 30):
            visible2 = False
            hide_time = time.time()
            print("đã chạmmmmmmmmmmmm")
            size1 += 10
            img1 = pygame.transform.scale(img1_raw, (size1, size1))
            score += 1  # Tăng điểm
            # eat_sound.play()  # Phát âm thanh khi ăn quả
    else:
        if time.time() - hide_time >= 1:
            x2 = random.randint(0, WIDTH - 30)
            y2 = random.randint(0, HEIGHT - 30)
            visible2 = True

    # Vẽ màn hình
    WINDOW.fill((255, 255, 255))
    WINDOW.blit(img1, (x1, y1))
    WINDOW.blit(img3, (x3, y3))

    if visible2:
        WINDOW.blit(img2, (x2, y2))
    # Hiển thị điểm số ở góc trên bên trái
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    WINDOW.blit(score_text, (10, 10))

    # Kiểm tra win
    if check_win(score):
        break

    # Kiểm tra thua
    if check_lose(x1, y1, x3, y3, size1, 100):
        break

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()