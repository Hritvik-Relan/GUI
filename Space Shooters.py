import tkinter as tk
import random
from PIL import ImageTk, Image
import time

# Set up the main window
root = tk.Tk()
root.title("Space Shooters")
root.geometry("1000x600")
root.resizable(False, False)

# Create the canvas
canvas = tk.Canvas(root, width=1000, height=600, bg="black")
canvas.pack()

# Load and resize background image (2000x1300)
background_img = Image.open("C:/Users/hritv/Downloads/bg1.jpg")
background_img = background_img.resize((2000, 1300))  # Resize background
background_img = ImageTk.PhotoImage(background_img)
canvas.create_image(0, 0, image=background_img, anchor="nw")

# Variables
spaceship = None
lasers = []
hyper_laser_ready = True
cooldown = 0
hyper_laser_duration = 0
counter = 0
game_over = False
asteroids = []
asteroid_count = 2  # Number of asteroids
asteroid_speed = [7] * asteroid_count  # Vertical speed for each asteroid

# Load and resize spaceship image (200x200)
spaceship_img = Image.open("C:/Users/hritv/Downloads/spaceship.png")
spaceship_img = spaceship_img.resize((200, 200))  # Resize spaceship
spaceship_img = ImageTk.PhotoImage(spaceship_img)
spaceship = canvas.create_image(500, 520, image=spaceship_img)

# Load and resize asteroid image (209x200)
asteroid_img = Image.open("C:/Users/hritv/Downloads/asteroid.png")
asteroid_img = asteroid_img.resize((209, 200))  # Resize asteroid
asteroid_img = ImageTk.PhotoImage(asteroid_img)

# Load and resize laser image (7x114)
laser_img = Image.open("C:/Users/hritv/Downloads/laser.jpg")
laser_img = laser_img.resize((7, 114))  # Resize laser
laser_img = ImageTk.PhotoImage(laser_img)

# Create multiple asteroids
def create_asteroids():
    for _ in range(asteroid_count):
        x = random.randint(50, 950)
        y = random.randint(-500, -50)
        asteroid = canvas.create_image(x, y, image=asteroid_img)
        asteroids.append(asteroid)

# Reset asteroid position
def reset_asteroid(asteroid):
    x_new = random.randint(50, 950)  # Reset to a random horizontal position
    y_new = random.randint(-500, -50)  # Start above the screen
    canvas.coords(asteroid, x_new, y_new)

# Movement functions
def move_spaceship(event):
    """Move the spaceship left or right."""
    x, y = canvas.coords(spaceship)
    if event.keysym == "d" and x < 950:
        canvas.move(spaceship, 20, 0)
    elif event.keysym == "a" and x > 50:
        canvas.move(spaceship, -20, 0)

root.bind("<d>", move_spaceship)
root.bind("<a>", move_spaceship)

# Shooting mechanism
def shoot():
    global lasers, cooldown
    if cooldown == 0:
        x, y = canvas.coords(spaceship)
        laser = canvas.create_image(x, y - 57, image=laser_img)  # Adjust laser start position
        lasers.append(laser)
        cooldown = 30  # Set cooldown to 30 frames (50ms per frame)

def shoot_hyper_laser():
    global counter, hyper_laser_duration
    if counter >= 5:  # Check if hyper laser can be activated
        counter -= 5  # Deduct 5 points for hyper laser activation
        hyper_laser_duration = 10  # Set the hyper laser duration to 10 seconds (200 frames)
        # Fire the hyper laser
        x, y = canvas.coords(spaceship)
        laser = canvas.create_image(x, y - 57, image=laser_img)
        lasers.append(laser)

root.bind("<space>", lambda _: shoot())
root.bind("<Control-Shift-space>", lambda _: shoot_hyper_laser())  # Bind hyper laser to Ctrl+Shift+Space

# Game over function
def game_over_screen():
    global game_over
    game_over = True
    canvas.delete("all")
    canvas.create_image(0, 0, image=background_img, anchor="nw")  # Show the background
    canvas.create_text(500, 250, text="GAME OVER", font=("Arial", 50), fill="red")
    canvas.create_text(500, 320, text=f"Points: {counter}", font=("Arial", 30), fill="white")
    canvas.create_text(500, 380, text="Press Esc to Exit", font=("Arial", 20), fill="white")

root.bind("<Escape>", lambda _: root.destroy())

# Cooldown and laser duration display
def update_cooldowns():
    global cooldown, hyper_laser_duration

    if cooldown > 0:
        cooldown -= 1  # Decrease the cooldown
    if hyper_laser_duration > 0:
        hyper_laser_duration -= 1  # Decrease the hyper laser duration

    # Show cooldowns
    canvas.delete("cooldown")
    if cooldown > 0:
        canvas.create_text(150, 50, text=f"Laser Cooldown: {cooldown // 10}", font=("Arial", 15), fill="white", tag="cooldown")
    if hyper_laser_duration > 0:
        canvas.create_text(150, 80, text=f"Hyper Laser: {hyper_laser_duration // 10} secs", font=("Arial", 15), fill="red", tag="cooldown")

# Main game loop
def update():
    global counter, game_over

    if not game_over:
        # Move asteroids
        for i, asteroid in enumerate(asteroids):
            canvas.move(asteroid, 0, asteroid_speed[i])
            ax, ay = canvas.coords(asteroid)

            # Reset asteroid if it moves off-screen
            if ay > 600:
                reset_asteroid(asteroid)

            # Check collision with spaceship
            sx, sy = canvas.coords(spaceship)
            if abs(sx - ax) < 100 and abs(sy - ay) < 100:
                game_over_screen()
                return

        # Move lasers
        for laser in lasers[:]:
            canvas.move(laser, 0, -20)
            lx, ly = canvas.coords(laser)

            # Remove laser if it moves off-screen
            if ly < 0:
                canvas.delete(laser)
                lasers.remove(laser)
                continue

            # Check collision with asteroids
            for asteroid in asteroids:
                ax, ay = canvas.coords(asteroid)
                if abs(lx - ax) < 60 and abs(ly - ay) < 110:  # Adjust hitbox for 7x114 laser size
                    reset_asteroid(asteroid)
                    canvas.delete(laser)
                    lasers.remove(laser)
                    counter += 1
                    break

        # Update score display
        canvas.delete("score")
        canvas.create_text(80, 30, text=f"Points: {counter}", font=("Arial", 20), fill="white", tag="score")

        # Update cooldowns and laser durations
        update_cooldowns()

        # Schedule the next frame
        root.after(50, update)

# Start the game
create_asteroids()
update()
root.mainloop()
