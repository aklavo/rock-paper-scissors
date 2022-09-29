import getpass
from player import player

print("-"*150)
print("Welcome to Rock-Paper-Scissors!")
print("-"*150)
print("The game is simple, each round a player will choose either rock, paper, or scissors in an attempt to beat their oppenent. First to win 3 rounds win.")
print("\nRules:\n -rock beats scissors\n -paper beats rock\n -scissors beats paper\n -ties result in a redo or round\n \n")
p1_name = input("Player 1 Enter your name: ")
p2_name = input("Player 2 Enter your name: ")
print("\nLet the game begin! For each round choose either rock, paper, or scissors. \n")

end_game_options = ['y','n']
choices = ['rock','paper','scissors']
win_conditions = {
      'rockpaper':2,
      'rockscissors':1,
      'paperrock':1,
      'paperscissors':2,
      'scissorsrock':2,
      'scissorspaper':1,
      'rockrock':0,
      'paperpaper':0,
      'scissorsscissors':0
}

# Intialize players
P1_wins = 0
P2_wins = 0
player_1 = player(p1_name,P1_wins,'rock')
player_2 = player(p2_name,P2_wins,'rock')

# Start game
addicted = 'y'
while addicted == 'y':
      round = 1
      player_1.wins = 0
      player_2.wins = 0
      while player_1.wins < 3 and player_2.wins < 3:
            # Promt P1
            player_1.current_choice = getpass.getpass("Player 1 Turn "+str(round)+" Choose: ")
            # Check if valid input
            if player_1.current_choice in choices:
                  # Promt P2
                  player_2.current_choice = getpass.getpass("Player 2 Turn "+str(round)+" Choose: ")
                  # Check if valid input
                  if player_2.current_choice in choices:
                        # Identify winner
                        scenario = player_1.current_choice + player_2.current_choice
                        winner = win_conditions[scenario]
                        # P1 wins
                        if winner == 1:
                              player_1.wins += 1
                              print("\nPlayer 1 chose "+player_1.current_choice+". Player 2 chose "+player_2.current_choice+".")
                              print("\nPlayer 1 wins round " +str(round)+"!\n")
                        # P2 wins      
                        elif winner == 2:
                              player_2.wins += 1
                              print("\nPlayer 1 chose "+player_1.current_choice+". Player 2 chose "+player_2.current_choice+".")
                              print("\nPlayer 2 wins round " +str(round)+"!\n")
                        # They tie
                        if winner == 0:
                              print("\nIt's a tie! Please try again.\n")
                        # Show choices and Scores      
                        print("Score:\n"+player_1.name+": "+str(player_1.wins)+"\n"+player_2.name+": "+str(player_2.wins))
                        # Did someone win?     
                        if player_1.wins == 3:      
                              winner_name = player_1.name
                        elif player_2.wins == 3:      
                              winner_name = player_2.name
                        # Go to next round
                        if player_1.wins < 3 and player_2.wins < 3:
                              print("\nNext Round!\n")
                        round+=1
                  else:
                        print("\nInvalid choice: Player 2 please enter either rock, paper, or scissors.\n")
            else:
                  print("\nInvalid choice: Player 1 please enter either rock, paper, or scissors.\n")
                  
      print("\nCongrats "+winner_name+"! You've won the game!")
      
      addicted = input("\nWould you like to play again [y/n]?\n")
      while addicted not in end_game_options:
           print("\nInvalid choice: Please enter either y or n.\n") 
           addicted = input("\nWould you like to play again [y/n]?\n")
      if addicted == 'y':
            print("\nDon't stop till ur numb!\n")
            
print("\nThanks for playing!")           