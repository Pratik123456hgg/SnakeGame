# 🐍 Classic Snake Game

A simple and fun implementation of the timeless Snake game built with Pygame. Guide your snake, eat food to grow, and avoid hitting the walls or yourself\!

-----

## ✨ Features

  * **Classic Gameplay:** Experience the nostalgic joy of the original Snake game.
  * **Growing Snake:** Your snake grows longer with each piece of food it eats.
  * **Boundary Collision:** Game over if you hit the edges of the screen.
  * **Self-Collision:** Game over if the snake collides with its own body.
  * **Score Tracking:** Keep an eye on your current score.
  * **High Score:** Track your best score across multiple game sessions.
  * **Basic Sound Effects:** Engaging background music and sound effects for eating and game over.
  * **Intuitive Controls:** Simple arrow key controls for movement.

-----

## 🎮 How to Play

1.  **Move the Snake:** Use the **Arrow Keys** (Up, Down, Left, Right) to control the snake's direction.
2.  **Eat Food:** Guide the snake to the red food squares. Each time you eat food, your snake will grow longer, and your score will increase.
3.  **Avoid Collisions:**
      * Don't hit the **edges of the game screen**.
      * Don't run into **your own snake's body**.
4.  **Game Over:** If you collide with the walls or yourself, the game ends.
5.  **Restart:** After "Game Over," press `R` to restart a new game or `Q` to quit.

-----

## 🚀 Getting Started

To run this game on your local machine, follow these steps:

### Prerequisites

Make sure you have Python installed. This project uses **Python 3.x**.

You'll also need `Pygame`, the library used for game development. Install it using pip:

```bash
pip install pygame
```

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Pratik123456hgg/SnakeGame.git
    cd SnakeGame
    ```

2.  **Place assets:** Ensure you have the necessary image and sound files (`snake.png`, `fruit.png`, `background.png`, `game_background.mp3`, `game_eat.mp3`, `game_over.mp3`) in the same directory as your Python script.

### Running the Game

Execute the main Python script:

```bash
python main.py
```

-----

## 📁 Project Structure

```
.
├── main.py                   # Your main game script
├── snake.png                 # Game icon
├── fruit.png                 # Food image
├── background.png            # Background image for game over screen
├── game_background.mp3       # Background music
├── game_eat.mp3              # Sound effect for eating food
└── game_over.mp3             # Sound effect for game over
├── README.md
└── LICENSE                   # (Optional) License file
```

-----

## 📄 License

This project is open source and available under the [MIT License](https://github.com/Pratik123456hgg/SnakeGame/blob/main/LICENSE).

-----

## 🙏 Acknowledgments

  * Inspired by classic arcade Snake games.
  * Developed using the [Pygame](https://www.pygame.org/) library.
