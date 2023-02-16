import pygame
import random

# initialize Pygame
pygame.init()

# set up the display
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Odd or Even")

# set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set up fonts
FONT = pygame.font.Font(None, 36)

# set up game variables
score = 0
rounds_played = 0

# main game loop
running = True
while running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                guess = "odd"
            elif event.key == pygame.K_e:
                guess = "even"
            else:
                guess = None

    # generate a random number and determine if it's odd or even
    number = random.randint(0, 9)
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"

    # check if the user guessed correctly and update the score
    if guess == result:
        score += 2
    else:
        score -= 1

    # increment the number of rounds played
    rounds_played += 1

    # clear the screen
    screen.fill(BLACK)

    # draw the score and number of rounds played
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    rounds_text = FONT.render(f"Rounds: {rounds_played}", True, WHITE)
    screen.blit(rounds_text, (10, 50))

    # draw the guess and result if they exist
    if guess:
        guess_text = FONT.render(f"Your guess: {guess}", True, WHITE)
        screen.blit(guess_text, (10, 100))
    result_text = FONT.render(f"The result was: {result}", True, WHITE)
    screen.blit(result_text, (10, 150))

    # update the display
    pygame.display.update()

# quit Pygame
pygame.quit()
