# %%
import random
import time
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    guess = " "
    count_down = int(7)
    previous_time = time.time()
    while count_down >= 0: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)

        #Display count down
        cv2.putText(frame, f'Time: {count_down}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,165,0), 2)

        #Display text on screen
        cv2.putText(frame, f'You choose: {guess}', (50, 90), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0), 2)

        cv2.imshow('frame', frame)
       
        if np.argmax(prediction[0])==0:
            guess = 'rock'
        elif np.argmax(prediction[0])==1:
            guess = 'paper'
        elif np.argmax(prediction[0])==2:
            guess = 'scissors'
        elif np.argmax(prediction[0])==3:
            guess = 'nothing'

        #Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        current_time = time.time()
        if int(current_time - previous_time) >= 1:
          previous_time = current_time
          count_down = count_down - 1

    return guess    
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def get_computer_choice():
  options=["rock", "paper", "scissors"]
  random_selection = random.choice(options)
  return random_selection

def get_winner(computer_choice, user_choice):
  winner = " "
  if computer_choice=="rock" and user_choice=="scissors":
    winner = "You lost"
  elif computer_choice=="rock" and user_choice=="paper":
    winner = "You won!"
  elif computer_choice=="sciccors" and user_choice=="rock":
    winner = "You won!"
  elif computer_choice=="sciccors" and user_choice=="paper":
    winner = "You lost"
  elif computer_choice=="paper" and user_choice=="rock":
    winner = "You lost"
  elif computer_choice=="paper" and user_choice=="scissors":
    winner = "You won!"
  elif computer_choice==user_choice:
    winner = "It is a tie!"
  return winner
  
def play_two():
  computer_wins = 0
  user_wins = 0
  result = " "
  while True:
    computer_choice=get_computer_choice()
    user_choice=get_prediction()
    result = get_winner(computer_choice, user_choice)
    if result=="You lost":
      computer_wins +=1
    elif result=="You won!":
      user_wins +=1
    
    print(f"The computer's choice was {computer_choice}")
    print(f"Your choice was {user_choice}")
    print(f"The computer has now won : {computer_wins} times")
    print(f"You have won : {user_wins} times")

    #break the loop when either computer or user won three times
    if computer_wins==3 or user_wins==3:
      break

  if computer_wins==3:
    print("You lost")
  elif user_wins==3:
    print("You won!")

  

play_two()



