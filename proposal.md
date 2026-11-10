# Video Background Rain Creator

## Repository
https://github.com/CalvinVan/PFDA2305_Final_Project

## Description
1-2 sentence description of what it will do and how it relevant to media and digital arts.
The following project should turn a still image into a video / gif of a background with animated trails based on 1 - 3 colors of the image. User's should be able to also choose between 3 pattern types of rain, spirals, and zig-zags. 

It is relevant to media / digital arts by transforming a still image and giving it more life and chaaracter by adding in motion through rain/trail effects using the colors of the image. 

## Features
- Feature 1
	- User should be able to import / place an image inside a designated folder. The program should then use said image to create a gif of the background with trail particles to give the image life.
- Feature 2
	- Users should be prompted at the beginning of executing the program on what sort of particle pattern is wanted by the user (rain, zig-zag, or spiral) and the program should implement said pattern in the image
- Feature 3
	- Users should also be prompted to input how many colors they want to see exhibited by the particle (1-3) and the program should then use said colors.

## Challenges
- Figuring out how to make a spiral pattern trail
- Investigate if pillow or some python library has functionality to figure out the major colors of a pattern and store it as an rgb to be used for the spirals
- Figure out how to make the pattern trails come from multiple directions possibly instead of just from the top.

## Outcomes
Ideal Outcome:
- The ideal outcome is that the user can give a photo in a folder and give input on the spiral pattern and number of colors in which the program should then generate a ~5 second gif
of the animated background.

Minimal Viable Outcome:
- The minimal viable outcome is that at the very least that the program is able to create a gif of an image of their choosing and at least 1 trail type (whether it be rain, zig-zag, or spiral) is implemented.

## Milestones

- Week 1
  1. Setup structure for the repository
  2. Setup skeleton code for the project and what initial classes / functions will be needed for the project 
  3. Setup basic file opening structure.
  4. Figure out which libraries / imports will be needed for the project

- Week 2
  1. Implement the video saving feature with a still image first
  2. Implement a basic rain pattern
  3. Implement the number of colors for the image
  4. Implement a zig zag pattern

- Week N (Final)
  1. Implement the spiral pattern for the image
  2. Create a demo video of the completed project