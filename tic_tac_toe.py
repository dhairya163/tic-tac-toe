from random import randint
a=[1,2,3,4,5,6,7,8,9]

print("Welcome to Tic-Tac-Toe!!\n",flush=True)

def draw_board():
  print(' '+str(a[0])+' '+'|'+' '+str(a[1])+' '+'|'+' '+str(a[2])+' ')
  print('---'+'|'+'---'+'|'+'---')
  print(' '+str(a[3])+' '+'|'+' '+str(a[4])+' '+'|'+' '+str(a[5])+' ')
  print('---'+'|'+'---'+'|'+'---')
  print(' '+str(a[6])+' '+'|'+' '+str(a[7])+' '+'|'+' '+str(a[8])+' ')
  print("\n")

count=0

def user_input():
    if count<7:
      print("You are playing as X , Enter your input from 1-9: ")
      user_inputs=int(input())-1
      while a[user_inputs] in ('O','X'):
        print("Oops that block is already taken!! Enter new Value ")
        user_inputs=int(input())-1
      a[user_inputs]='X'
    else:
      print("The game is a TIE")
    draw_board()

def computer():
  num=randint(0,8)
  while a[num] in ('X','O'):
    num=randint(0,8)
  a[num]='O'
  print("The computer has completed its turn: \n")
  draw_board()

def check():
  global count
  for i in range(0,11):
    if (a[0]==a[1]==a[2]):
      print(f"{a[0]} WON THE GAME!!")
      break
    elif (a[0]==a[3]==a[6]):
      print(f"{a[0]} WON THE GAME!!")
      break
    elif (a[0]==a[4]==a[8]):
      print(f"{a[0]} WON THE GAME!!")
      break
    elif (a[1]==a[4]==a[7]):
      print(f"{a[1]} WON THE GAME!!")
      break
    elif (a[2]==a[5]==a[8]):
      print(f"{a[2]} WON THE GAME!!")
      break
    elif (a[6]==a[4]==a[2]):
      print(f"{a[6]} WON THE GAME!!")
      break
    elif (a[6]==a[7]==a[8]):
      print(f"{a[6]} WON THE GAME!!")
      break
    elif (a[3]==a[4]==a[5]):
      print(f"{a[3]} WON THE GAME!!")
      break
    else:
        user_input()
        if count<4:
          computer()
          count+=1
        else:
          if (a[0]==a[1]==a[2]):
            print(f"{a[0]} WON THE GAME!!")
            break
          elif (a[0]==a[3]==a[6]):
            print(f"{a[0]} WON THE GAME!!")
            break
          elif (a[0]==a[4]==a[8]):
            print(f"{a[0]} WON THE GAME!!")
            break
          elif (a[1]==a[4]==a[7]):
            print(f"{a[1]} WON THE GAME!!")
            break
          elif (a[2]==a[5]==a[8]):
            print(f"{a[2]} WON THE GAME!!")
            break
          elif (a[6]==a[4]==a[2]):
            print(f"{a[6]} WON THE GAME!!")
            break
          elif (a[6]==a[7]==a[8]):
            print(f"{a[6]} WON THE GAME!!")
            break
          elif (a[3]==a[4]==a[5]):
            print(f"{a[3]} WON THE GAME!!")
            break
          else:
            print("\n\nTHE GAME IS A TIE!!!\n\n")
            break
      

draw_board()
check()