
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#logic">Logic</a></li>
        <li><a href="#ai">AI</a></li>
        <li><a href="#learning">Learning</a></li>
      </ul>
    </li>
        <li><a href="#built-with">Built With</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#clone-the-project">Clone the Project</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#run-the-program">Run the Program</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Quoridor is a 2 or 4-player intuitive strategy game designed by Mirko Marchesi and published by Gigamic Games. You can read more about this game [here](https://en.wikipedia.org/wiki/Quoridor). 
This project has 3 parts: Logic, AI and Learning.

### Logic
This part of Project is a simple multi-player quoridor game. It has 2-players and 4-players mode and you can play it with your friends.

### AI
In this part you are playing with an AI-based opponent. This AI agent uses minimax tree and alpha-beta pruninig algorithms. This part has 2-players and 4-players mode too.

### Learning
In this part AI agents play together to gain experience. In the end, the AI agents which had the best functionality will be the winner of the course. You can see details about thses matches in the log files in Learning folder. This part uses multi-threads to speed op the program.

### ScreenShots
<img width="1065" height="1016" alt="image" src="https://github.com/user-attachments/assets/e7ecb67f-9950-4bd6-9737-d138ad0098c7" />





## Built With

The whole project is built with python. Even for graphic parts of project we used pygame.
* [python](https://www.python.org/)
* [pygame](https://www.pygame.org/)


<!-- GETTING STARTED -->
## Getting Started

At the first place, you need to download the project. You can dowanload it completely as a zip file or do the following commands.



### Clone the Project

Run following commands in your terminal
  ```sh
  git clone https://github.com/MRSadeghi78/Quoridor.git
  ```
Enter the project directory
  ```sh
  cd Quoridor
  ```

### Installation

Make sure you have this instalations in your computer separately
   ```sh
   python -m venv .venv
   ..venv\Scripts\Activate.ps1
   pip install pygame
   ```
If the version of python didn't show up, install python using following command in linux
   ```sh
   sudo apt-get update
   sudo apt-get install python3.6
   ```
Or if you use windows, download it from [here](https://www.python.org/downloads/windows/)

### Run the Program

First enter the project directory, then run the following command:
   ```sh
   python Main.py
   ```
The work is done! Enjoy the game :)   

<!-- USAGE EXAMPLES -->
## Controls Explanation

Game Objective: The goal is to be the first player to move your pawn to any square on the opposite side of the board.
Player Turn: The game is turn-based. The color of the current player is shown in the top-left corner of the screen.
Mouse Controls:
Show Possible Moves: Click on your pawn to see all the possible squares you can move to, which will be highlighted in light gray.
Move Your Pawn: Once the possible moves are highlighted, click on any of the light gray squares to move your pawn to that position.
Place a Wall:
Vertical Wall: To place a wall vertically, click on the thin space between two adjacent squares.
Horizontal Wall: To place a wall horizontally, click on the thin space above or below a square. You have a limited number of walls, displayed next to your player name.
Winning the Game: When a player wins, a "You win the game" message will appear. You can then click the "Play again" button to start a new match.


## Demo Videos link:

[Video1](https://drive.google.com/file/d/10MdWx50euly_ig8aeTnuonoDgjzcV69m/view?usp=sharing)

[Video2](https://drive.google.com/file/d/1MdUVTi6YMI8Asxv3vxWL0C8vJRGgrEQj/view?usp=sharing)

<!-- LICENSE -->
## License

Distributed under the Apache License. See `LICENSE` for more information.


