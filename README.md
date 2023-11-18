# Rubik's cube solver

## Motivation for this project
I have always been fascinated by solving rubik's cubes, the thought of holding one of the ~43 quintillion different permutations and with a certain algorithm ('cubing' jargon for a set of steps to solve a cube) arrive to the most famous permutation. To put that enormous number into perspective, if you had a standard-sizes rubik's cube (5.6 cms / 2.25" each edge) for each possible permutation, you could cover the surface of the earth 275 times, or stack them in a 261 light-year-tall ($`~2.4 \times 10^{15}`$ km) tower.

## Project description
This project is a final thesis for my HS computer science course. As the name suggests, this project solves a rubik's cube.<br> After showing each of the 6 faces of the cube to the camera, an algorithm will be printed to the screen.

## How to project works
After opening the application the user scans all 6 sides of the rubik's cube with the computer camera (external camera for PCs, built-in camera for laptops). After scanning the rubik's cube, the computer will output a series of moves (using singmaster notation) that solves the rubik's cube.

## Target Audience
This project is for anyone that wants to solve a rubik's cube

## Constraints and requirements 
Of course, the most obvious requirement is having a rubik's cube to solve. <br> There are not many requirements for this project, the only hardware you need it a functioning camera (built-in laptop camera works fine). The only software requirement is that python, the opencv library and the numpy library are installed. <br> There are only 2 constraints on the project, one is the quality of the camera, if the camera quality is really poor then the computer will have a hard time detecting the rubik's cube. The other constraint is the computer's computation speed, any laptop (or better) is fine, but a slow computer will lead to  a slower output.