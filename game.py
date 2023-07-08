def analyzeboard():
  return 1
  
def main():
  choice = input("enter 1 if you want to play single player , 2 for Multi player: ");
  choice=int(choice)
  board=[0, 0, 0, 0, 0, 0, 0, 0, 0]
  if(choice==1):
    print('you are playing against computer');
    print('Computer: O and You: X');
    player = input("press 1 if you want first turn else press 0");
    player = int(player)
    for i in range(0,9):
      if(analyzeboard(board)!=0):
        break;
    
  
