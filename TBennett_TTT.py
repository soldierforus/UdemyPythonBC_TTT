import sys
game = ['','','','','','','','','']
p1 = 'Player 1'
p2 = 'Player 2'    

def board():
    print '''
  ___________
('   |   |   ')
(' 0 | 1 | 2 ')
('___|___|___')
('   |   |   ')
(' 3 | 4 | 5 ')
('___|___|___')
('   |   |   ')
(' 6 | 7 | 8 ')
('___|___|___')

'''

def gameOver():
    if game[0] == 'X' and game[1] == 'X' and game[2] =='X' or game[3] ==' X' and game[4] == 'X' and game[5] =='X' or game[6] == 'X' and game[7] == 'X' and game[8] == 'X' or game[6] == 'X' and game[4] == 'X' and game[2] =='X'or game[0] == 'X' and game[4] == 'X' and game[8] =='X'or game[0] == 'X' and game[3] == 'X' and game[6] =='X'or game[1] == 'X' and game[4] == 'X' and game[7] =='X' or game[2] == 'X' and game[5] == 'X' and game[8] =='X':
        print p1, 'WINS!', '''
                                         
  ___ ____ ___ _  ___   ___ _  _____ ____
 / _ `/ _ `/  ' \/ -_) / _ \ |/ / -_) __/
 \_, /\_,_/_/_/_/\__/  \___/___/\__/_/   
/___/                                  
 '''
        return True
    if game[0] == 'O' and game[1] == 'O' and game[2] =='O' or game[3] == 'O' and game[4] == 'O' and game[5] =='O' or game[6] == 'O' and game[7] == 'O' and game[8] == 'O' or game[6] == 'O' and game[4] == 'O' and game[2] =='O'or game[0] == 'O' and game[4] == 'O' and game[8] =='O'or game[0] == 'O' and game[3] == 'O' and game[6] =='O'or game[1] == 'O' and game[4] == 'O' and game[7] =='O' or game[2] == 'O' and game[5] == 'O' and game[8] =='O':
        print p2, 'WINS!', '''
                                         
  ___ ____ ___ _  ___   ___ _  _____ ____
 / _ `/ _ `/  ' \/ -_) / _ \ |/ / -_) __/
 \_, /\_,_/_/_/_/\__/  \___/___/\__/_/   
/___/                                  
 '''
        return True
    elif '' not in game:
        print 'TIE', '''
        
  __  .__                                       
_/  |_|__| ____      _________    _____   ____  
\   __\  |/ __ \    / ___\__  \  /     \_/ __ \ 
 |  | |  \  ___/   / /_/  > __ \|  Y Y  \  ___/ 
 |__| |__|\___  >  \___  (____  /__|_|  /\___  >
              \/  /_____/     \/      \/     \/ 
        '''
        
def formatValue(val):
    return ' ' if val == '' else val

def printBoard(state):
    board = map(formatValue, state) 
    #Formats the values of state
    
    print '''
  ___________
('   |   |   ')
(' {0} | {1} | {2} ')
('___|___|___')
('   |   |   ')
(' {3} | {4} | {5} ')
('___|___|___')
('   |   |   ')
(' {6} | {7} | {8} ')
('___|___|___')

'''.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]);
    
def getMove():
    return raw_input("Please select your corresponding square using 0,1,2,3,4,5,6,7,8\r\n You selected: ")
    
def playA():
    print "\r\nYour move, ", p1
    n = getMove()
    if n not in ('0','1','2','3','4','5','6','7','8'):
        print "Please select a valid box number"
        n = getMove()
    elif game[int(n)] != '':
        print "Sorry, that box is already taken"
        n = getMove()
    else:
        game[(int(n))] = 'X'
        board()
        printBoard(game)
        if not gameOver():
            playB()
        else:
            sys.exit()
                            
def playB():
    print "\r\nYour move, ", p2
    n = getMove()
    if n not in ('0','1','2','3','4','5','6','7','8'):
        print "Please select a valid box number"
        n = getMove()
    elif game[int(n)] != '':
        print "Sorry, that box is already taken"
        n = getMove()
    else:
        game[(int(n))] = 'O'
        board()
        printBoard(game)
        if not gameOver():
            playA()
        else:
            sys.exit()
            
    
def start():
    print "Hello, and welcome to Travis' first python project - Tic Tac Toe!\r\n \r\nThis version requires two human players. Player One will move first as X and Player Two will be O."        
    print                '''\r\nMoves will be made by selecting the corresponding number with the box you want to mark
    
                          0 | 1 | 2            
                         -----------
                          3 | 4 | 5            
                         -----------
                          6 | 7 | 8
                        '''
    global p1
    p1 = raw_input('Player One Name:  ')
    global p2    
    p2 = raw_input('Player Two Name:  ')
    
    board()
    playA()
    
start()