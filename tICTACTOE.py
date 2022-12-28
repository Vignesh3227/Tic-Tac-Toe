def board(x,y):
    zero= 'X' if x[0] else ('O' if y[0] else 0)
    one='X' if x[1] else ('O' if y[1] else 1)
    two='X' if x[2] else ('O' if y[2] else 2)
    three='X' if x[3] else ('O' if y[3] else 3)
    four='X' if x[4] else ('O' if y[4] else 4)
    five='X' if x[5] else ('O' if y[5] else 5)
    six='X' if x[6] else ('O' if y[6] else 6)
    seven='X' if x[7] else ('O' if y[7] else 7)
    eight='X' if x[8] else ('O' if y[8] else 8)
    print(" ____ ____ ____")
    print("|    |    |    |")
    print(f"|  {zero} |  {one} | {two}  |")
    print(f"|----|----|----|")
    print(f"|  {three} |  {four} | {five}  |")
    print(f"|----|----|----|")
    print(f"|  {six} |  {seven} | {eight}  |")
    print("|____|____|____|")
    print()
    
def winner(x,y):
    global p1,p2
    wx=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wx:
        if(x[win[0]]+x[win[1]]+x[win[2]])==3:
            print()
            board(x,y)
            print(p1,"is the winner!!Congratulations!!")
            return 1
        if(y[win[0]]+y[win[1]]+y[win[2]])==3:
            print()
            board(x,y)
            print(p2,"is the winner!!Congratulations!!")
            return 0
    return -1    

while True:
    print('TIC-TAC-TOE!!')
    p1=input("Enter player 1's name: ")
    p2=input("Enter player 2's name: ")
    x=[0,0,0,0,0,0,0,0,0]
    y=[0,0,0,0,0,0,0,0,0]
    t=1
    c=0
    while True:
        board(x,y)
        if t==1:
            print(p1+"'s","turn")
            x1=int(input("Enter the plot number: "))
            x[x1]=1
            t=0
        else:
            print(p2+"'s turn")
            y1=int(input("Enter the plot number: ")) 
            y[y1]=1
            t=1
        c+=1    
        cwin=winner(x,y)
        if cwin != -1 or c==9:
            print('Match over')
            break
    print('New Game?')
    new=input("Enter yes or no: ")
    if new=="yes":
        continue
    else:
        print("See ya next time!")
        break
