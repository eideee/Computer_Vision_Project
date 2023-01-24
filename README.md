# Computer Vision Rock Paper Scissors Project Documentation

The game project would leverage on the Teachable Machine application made possible by Google. The application would allow the captured images to be analysed and recognised  by the computer as images that belong to Rock, Paper, Sciccors or idle gestures.
The written code should mimic the Rock,Paper Sciccors game by getting input manually via text as well as input through image and later decide the winner.

## Milestone 1 - Setup the environment
The project's repository was successfully created on GitHub.

## Milestone 2 - Create the computer vision system
The initial image files were created on Google's Teachablemachine. This Google's web-based machine learning platform was easy to use and the interfaces were quite friendly. The images were then trained to recognise the important gestures for Rock, Paper Sciccors game. 

## Milestone 3 - Install the depedencies
Utilised the package manager to instal the required library in order to allow for the game to run.

Virtual environtment was created by using Conda. Conda is also a package manager as well as an environment management system. 

Further check was conducted to verify if the imported and tranined image files could identify the gesture input captured by computer's camera. OpenCV and Tensorflow are amongst the imported library utilised to execute the game code.

Identified the representation of images in the list to classify which probability denote Rock, Paper or Sciccors gestures.

## Milestone 4 - Create a Rock-Paper-Sciccors Game
All the functions created in the earlier tasks were combined to make a complete code for the Rock-Paper-Sciccors game. This is the early version of the game which is to gather input through text from the user (player one) and compare it with the generated random choice represnting input from the computer (player two). 

## Milestone 5 - Use the camera to play Rock-Paper-Sciccors
The game has now evolved to the higher level. Input from computer is still being generated randomly, however input from the other player is being handled by capturing gestures via computer's camera. putText funtion from openCV library is being used to display text on the image. Text on the image would display the matching gesture on the screen with the earlier trained images. For example, if the user gesture for Rock, the code would verify with the prediction model if gesture matched with the trained Rock images, eventually the text on the screen would display that the user just made a Rock gesture.

Instead of single analysis of input from players, the game now permit number of transactions until either player won three times. As an another added feature, a counter is being displayed on the screen to indicate the remaining time for the user to make a choice (Rock,Paper or Sciccors). At the end of the end, the program would display the winner who has successfully secured three wins.

The picture below summarises the view of the input screen. Count down timer is being displayed on the first row. The second row indicate the matching gesture of the trained images.

![gui](https://user-images.githubusercontent.com/53040471/214426995-aacb8a75-636f-4077-aa3d-08863b6567a1.jpg)

![result](https://user-images.githubusercontent.com/53040471/214427159-444a80d6-219a-4842-a197-f7fd4f36dcb2.jpg)

