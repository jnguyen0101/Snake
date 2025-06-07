# Snake Game
A classic Snake game implemented in Python using the built-in `turtle` graphics library.

## Features
- Core Snake gameplay mechanics
- Control using the arrow keys
- Collision detection with walls and self
- Score tracking and display

## Technologies Used
- Python 3.12
- `turtle` (standard library module)

## Getting Started

### Prerequisites

Make sure you have Python 3 installed:

```bash
python --version
```

The game uses only the built-in `turtle` module, so no additional installations are needed.

### Running the Game

Clone or download the repository, then run:

```bash
python main.py
```

A window will open showing the game screen.

## How to Play
- Use the **Arrow Keys** on your keyboard to move the snake:
  - **↑** Move up
  - **↓** Move down
  - **←** Move left
  - **→** Move right
- Eat the red food circles to grow longer and increase your score
- Avoid running into:
  - The walls (edges of the screen)
  - Your own body
- The game ends when the snake collides with either
- Your current score is displayed at the top

## Project Structure

```
Snake/
│
├── food.py          # Food generation and placement
├── main.py          # Main game file
├── scoreboard.py    # Score tracking and display
├── snake.py         # Snake class and movement logic
├── README.md
```
