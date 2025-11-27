# Bouncing_Ball
Bouncing Ball is a classic arcade-style game developed in Python using the Pygame library. The player controls a paddle at the bottom of the screen to keep a bouncing ball from falling off the screen. The objective is to score points by hitting the ball with the paddle while the ball speed and difficulty increase progressively as you score more.
*

# Bouncing Ball Game 🏀

A simple and addictive arcade-style game built with Python and Pygame. Control a paddle at the bottom of the screen to keep a ball bouncing. Score points by hitting the ball, while the ball speed and difficulty progressively increase to challenge your reflexes.

This project serves as a fun introduction to game development with Pygame, demonstrating key concepts like event handling, collision detection, dynamic difficulty, and real-time rendering.

*

### 🎮 Features

- Speed selection menu before starting, with three difficulty levels: Slow, Normal, Fast  
- Smooth paddle movement controlled by Left and Right arrow keys  
- Increasing ball speed every 5 points scored to raise difficulty progressively  
- On-screen display of current score and level, updating in real time  
- Automatic game reset when the ball falls below the paddle  
- Simple, clean graphics with contrasting colors for clear gameplay  

*

### 🚀 How It Works

- When launched, the game provides a speed menu for the player to select initial difficulty.  
- The ball moves bouncing off the walls and paddle. The paddle is controlled horizontally by arrow keys.  
- Each time the ball hits the paddle, the score increments by 1. After every 5 points, the ball speed increases by 20%, making the game more challenging.  
- If the ball falls past the paddle, the score and level reset, and the ball restarts in the center with initial speed.  
- The game runs smoothly at 60 frames per second using Pygame’s clock mechanism.  

*

### 🛠️ Tech Stack

- Python 3.x  
- Pygame: handles graphics rendering, keyboard input, collision detection, and main game loop  

*

### 📦 Installation

1️⃣ Clone the repository 
bash
https://github.com/yourusername/bouncing-ball-game.git

2️⃣ Make sure you have Pygame installed (if not, install it using pip):  
bash
pip install pygame


3️⃣ Run the game script:  
bash
python bouncing_ball_game.py


*

### 🖥️ Output

- A game window opens with a blue background.  
- Paddle is white and located near the bottom.  
- Ball is red and moves with initial speed based on the selected level (slow, normal, or fast).  
- Player’s current score and level are displayed on the top-left corner in yellow.  
- The ball bounces off screen edges and paddle, speeding up as levels increase.  
- If the ball misses the paddle, the game resets score and level, and the ball returns to the center.  

*

### 🎮 Controls

| Key          | Action            |
|--------------|-------------------|
| Left Arrow   | Move paddle left  |
| Right Arrow  | Move paddle right |
| ESC          | Exit the game     |

*

### 📜 License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code for personal and commercial projects with proper attribution.

*

### 👨‍💻 Author

Ashish Kumar Prajapati

*
