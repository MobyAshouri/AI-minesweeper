By: Moby Ashouri and Maymunah Hicks

## CS 420: Gen AI Minesweeper

### Overview

In our Minesweeper game project, we employed several foundational software design principles to enhance the game's functionality and maintainability. Our approach was centered on making the game adaptable and organized, utilizing the Open Closed Principle, Model-View-Controller (MVC) framework, Event-Driven Programming, and the concept of States.

### Enforced Open Closed Principle

We designed our game with adaptability in mind, enabling customization of key game settings like the grid size and number of mines through initial parameters. This adherence to the Open Closed Principle allows for future expansions and modifications without necessitating rewrites of existing code, which makes it easier for easier updates and enhancements. The disadvantage here is a potential increase in complexity when incorporating new features, but this complexity is offset by the benefits of scalability and flexibility.

### MVC

The game's architecture is separated into an MVC pattern,  the game logic (Model), user interface (View), and input handling (Controller) into distinct components. This separation wasn't initially intentional but became apparent as development progressed, providing a clear organizational framework that simplifies modifications and maintenance. However, applying MVC in its entirety may be somewhat excessive for a simple Tkinter-based application, introducing unnecessary complexity into the project.


### Event Driven Programming

A feature in our Minesweeper game that is enabled by Event Driven Programming is the ability to place flags on tiles by right clicking. This approach enhances the game's interactivity and user engagement by responding to user's actions real time. The challenge here lies in ensuring clarity and accessibility for all users, which necessitates comprehensive documentation and intuitive design. 


### States

State management is utilized to monitor and respond to changes in the game's status, such as determining when a game ends due to a mine being triggered. By effectively managing game states, we can create more coherent and enjoyable game experience. While this adds a degree of complexity to the games logic, it is crucial for structuring the gameplay dynamics efficiently.
