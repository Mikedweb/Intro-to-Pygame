# Installation and setup 2
# import pygame, sys

# # Set up everything Pygame related
# pygame.init()


# Game components 2
# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()


# Game components 3
# # Clock for setting FPS
# clock = pygame.time.Clock()

# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()

#   # Tick the clock according to the framerate (60)
#   clock.tick(60)
#   # Get previous time
#   previous_time = clock.get_time()
#   # Get current FPS (probably won't always be exactly 60)
#   fps = clock.get_fps()
#   print(previous_time)
#   print(fps)


# Game components 4
# # Game screen (surface)
# screen = pygame.display.set_mode((200, 100))
# # Set the game caption
# pygame.display.set_caption("My Special Game")

# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()

#   # Set the screen color to white
#   screen.fill("white")
#   # Redraw the entire display
#   pygame.display.flip()
#   # Redraw the entire display if no parameter passed in or pass in a Rect to redraw only everything within that Rect
#   # pygame.display.update()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Drawing 1
# # Create color via string
# orange = "orange"
# # Create color via RGBA values, max = 255, min = 0, max for A = 1
# white = pygame.Color(255, 255, 255, 1)
# red = pygame.Color(255, 0, 0, 1)
# purple = pygame.Color(255, 0, 255, 1)

# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()

#   # Set the screen color
#   screen.fill(purple)
#   screen.fill(orange)
#   screen.fill(white)
#   screen.fill(red)
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Drawing 2
# Rectangle with x=50, y=10, width=200, height=100, x and y are coordinates of top left corner
# rect = pygame.Rect(50, 10, 200, 100)

# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()

#   # Set the screen color
#   screen.fill(background_color)
#   # Draw a filled in rectangle
#   pygame.draw.rect(screen, "red", rect)
#   # Draw a hollow, curved corner rectangle
#   pygame.draw.rect(screen, "red", rect, 5, 20)
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Drawing 3
# # Coordinates of points of triangle
# triangle_coordinates = [(100, 50), (125, 100), (75, 100)]

# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()

#   # Set the screen color
#   screen.fill(background_color)
#   # Draw a circle by passing in coordinates of center of circle (x=100, y=100) and radius=50
#   # pygame.draw.circle(screen, "blue", (100, 100), 50)
#   # Draw a polygon by passing in coordinates of corners. Pygame connects edges with lines in order of the corner coordinates
#   pygame.draw.polygon(screen, "yellow", triangle_coordinates)
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Drawing 4
# # Load the image
# apple = pygame.image.load("apple.png")
# # Get the image rectangle
# apple_rect = apple.get_rect()
# # Update the x and y of the rectangle
# apple_rect.x = 50
# apple_rect.y = 100

# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()

#   # Set the screen color
#   screen.fill(background_color)
#   # Draw rectangle around image
#   pygame.draw.rect(screen, "black", apple_rect, 1)
#   # Draw the image
#   screen.blit(apple, apple_rect)
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Drawing 5
# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()

#   # Set the screen color
#   screen.fill(background_color)
#   # Draw a single diagonal line
#   # pygame.draw.line(screen, "red", (50, 50), (200, 100), 5)
#   # Draw an N by connecting multiple points
#   pygame.draw.lines(screen, "blue", False, [(50, 250), (50, 50), (250, 250), (250, 50)], 5)
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Drawing 6
# import pygame, sys, math
# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()

#   # Set the screen color
#   screen.fill(background_color)
#   # Draw ellipse-bounding Rect
#   pygame.draw.rect(screen, "black", pygame.Rect(50, 50, 100, 200), 1)
#   # Draw ellipse
#   pygame.draw.ellipse(screen, "green", pygame.Rect(50, 50, 100, 200))
#   # Draw arc-bounding Rect
#   pygame.draw.rect(screen, "black", pygame.Rect(50, 50, 100, 100), 1)
#   # Draw arc
#   pygame.draw.arc(screen, "purple", pygame.Rect(50, 50, 100, 100), math.pi, 0, 5)
#   # Redraw the entire display
#   pygame.display.flip()


# Drawing 7a
# rect = pygame.Rect(100, 50, 100, 100)
# # Manually update x and y
# # rect.x = 150
# # rect.y = 100
# # Move left by 50 down by 50
# # rect = rect.move(-50, 50)
# # Increase width by 100 and height by 100
# # rect = rect.inflate(100, 100)
# # Decrease with by 75 and height by 75
# # rect = rect.inflate(-75, -75)
# # Set new x, y, width, and height values
# rect.update(50, 100, 200, 150)

# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()
  
#   # Set the screen color
#   screen.fill(background_color)
#   # Draw rectangle
#   pygame.draw.rect(screen, "blue", rect)
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Drawing 7b
# apple = pygame.image.load("apple.png")
# rect = apple.get_rect()
# # Increase initial x and y by 100
# rect = rect.move(100, 100)
# # Increase width and height by 200
# apple = pygame.transform.scale(apple, (200, 200))
# # Rotate image by 180 degrees
# apple = pygame.transform.rotate(apple, 180)

# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()
  
#   # Set the screen color
#   screen.fill(background_color)
#   # Draw the apple
#   screen.blit(apple, rect)
#   # screen.blit(apple, apple.get_rect())
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Movement 1
# apple = pygame.image.load("apple.png")
# rect = apple.get_rect()
# rect = rect.move(50, 50)
# circle_x = 50
# circle_y = 50

# Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()

#   # Continuously update the x and y positions by 1 with each loop iteration (60x per second)
#   # rect = rect.move(1, 1)
#   circle_x += 1
#   circle_y += 1
  
#   # Set the screen color
#   screen.fill(background_color)
#   # screen.blit(apple, rect)
#   pygame.draw.circle(screen, "red", (circle_x, circle_y), 50)
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Movement 2 (Parts 1 and 2)
# apple = pygame.image.load("apple.png")
# rect = apple.get_rect()
# rect = rect.move(10, 10)
# # Game screen rect
# screen_rect = screen.get_rect()
# # Point to collide with
# point = (150, 15)
# # Obstacle to collide with
# obstacle = pygame.Rect(0, 200, 100, 10)


# # Return true if collision detected
# def check_for_collision():
#   # Check if overlap between the left, right, top, or bottom sides of the rect and the screen
#   if rect.x <= 0 or rect.x + rect.width >= screen_rect.width or rect.y <= 0 or rect.y + rect.height >= screen_rect.height:
#     return True
#   # Check if overlap between a rect and another rect
#   if rect.colliderect(obstacle):
#     return True
#   # Check if overlap between a rect and a point
#   if rect.collidepoint(point[0], point[1]):
#     return True
#   return False


# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()

#   # Move the apple only if no collision detected
#   if not check_for_collision():
#     rect = rect.move(1, 0)
  
#   # Set the screen color
#   screen.fill(background_color)
#   # Draw the obstacle
#   pygame.draw.rect(screen, "red", obstacle)
#   # Draw the apple
#   screen.blit(apple, rect)
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Events 1
# # Background color
# background_color = "white"

# circle_x = None
# circle_y = None

# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()
#     # Triggered when the user presses down on a mouse button
#     if event.type == pygame.MOUSEBUTTONDOWN:
#     # Get position of mouse on screen
#       pos = pygame.mouse.get_pos()
#       circle_x = pos[0]
#       circle_y = pos[1]
#     # Triggered when the user releases a mouse button
#     if event.type == pygame.MOUSEBUTTONUP:
#       print("Mouse up")

#   # Set the screen color
#   screen.fill(background_color)
#   if circle_x != None and circle_y != None:
#     pygame.draw.circle(screen, "purple", (circle_x, circle_y), 25)
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)


# Events 2
# # Background color
# background_color = "white"

# circle_x = 50
# circle_y = 50

# # Start our run loop
# while True:
#   # Listen for all events currently occurring
#   for event in pygame.event.get():
#     # Check if there is a quit event (triggered by pressing the close button)
#     if event.type == pygame.QUIT:
#       # Shut down Pygame
#       pygame.quit()
#       # Exit the system
#       sys.exit()
#     # Detect when any key was pressed down
#     # if event.type == pygame.KEYDOWN:
#     #   if event.key == pygame.K_LEFT:
#     #     print("Left keydown")
#     # Detect when any key was released
#     # if event.type == pygame.KEYUP:
#     #   print("Keyup")

#   # Get list of keys currently being pressed
#   keys = pygame.key.get_pressed()
#   # Each case returns true if that key is currently being pressed
#   if keys[pygame.K_LEFT]:
#     circle_x -= 1
#   if keys[pygame.K_RIGHT]:
#     circle_x += 1
#   if keys[pygame.K_UP]:
#     circle_y -= 1
#   if keys[pygame.K_DOWN]:
#     circle_y += 1
  
#   # Set the screen color
#   screen.fill(background_color)
#   # Draw a circle
#   pygame.draw.circle(screen, "purple", (circle_x, circle_y), 25)
#   # Redraw the entire display
#   pygame.display.flip()
  
#   # Tick the clock according to the framerate (60)
#   clock.tick(60)
