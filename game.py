def analyzeboard():
  return int(0)
def CompTurn():
  return 1
def ConstBoard(board):
  print("current state of the board \n\n")

  for i in range(0,9):
    if((i>0) and (i%3==0)):
      print('\n')
    if(board[i]==0):
      print('_ ')
    if(board[i]==-1):
      print('X ')
    if(board[i]==1):
      print('O ')

def User1Turn(board):
  pos=input('Enter a position for X from [1,2......9]');
  pos=int(pos)-1;
  if(board[pos]!=0):
    print("Wrong Move")
    exit(0);
    board[pos-1]=-1


def User2Turn(board):
  pos=input('Enter a position for O from [1,2......9]');
  pos=int(pos)-1;
  if(board[pos]!=0):
    print("Wrong Move")
    exit(0);
    board[pos-1]=1


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
      if((i+player)%2==0):
        CompTurn(board);
      else:
        ConstBoard(board);
        User1Turn(board);
    else:
      for i in range(0,9):
        if(analyzeboard(board)!=0):
          break;
        if(i%2==0):
          CompTurn(board);
        else:
          ConstBoard(board);
          User2Turn(board);
  x=analyzeboard(board)
  if(x==0):
    ConstBoard(board);
    print("DRAW");
  if(x==-1):
    ConstBoard(board);
    print("PLayer X wins ");
  if(x==1):
    ConstBoard(board);
    print("Player O wins");
