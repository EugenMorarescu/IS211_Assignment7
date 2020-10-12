import random
import sys

class Player:
    def __init__(self,name):
        self.name=name
        self.hold=False
        self.roll=True
        self.turn=False
        self.total_score=0
        
    def r_or_h(self):
        ans = input("{} do you want to Roll ('r') or Hold ('h')? ".format(self.name))
        ans = ans.lower()
        
        if ans == 'r':
            self.hold=False
            self.roll = True
            return('roll')
            
        
        if ans =='h':
            self.hold = True
            self.roll=False
            return('hold')
            
        else:
            print('Wrong input, try again please')
            
            
class Die:
    def __init__(self):
        self.num=0

    def roll(self):
        self.num = random.randint(1,6)
        return self.num
    
class Game:
    def __init__(self,num_players):
        self.num_players=num_players
        self.players =[]
        self.die=Die()
        self.p1_score=0
        self.p2_score=0
        self.temp_score=0
        self.pcount=0
        
        for i in range(1,num_players+1):
            player=Player('Player ' + str(i))
            self.players.append(player)

        self.current=self.players[self.pcount]
        print(self.current.name + ' Starts!')
        
        self.go()
        
    def go (self):
        roll_score = self.die.roll()
        if (roll_score == 1):
            self.temp_score = 0
            print("\n{} rolled a {}, no points for you!\nYour current turn score is {}\nYour total score is {}\n".format(self.current.name,roll_score,self.temp_score,self.current.total_score))
            input("Press Enter to continue\n")
            self.scores()
            
            
        else:
            self.temp_score+=roll_score
            print("\n{} rolled a {}\nYour current turn score is {}\nYour total score is {}".format(self.current.name,roll_score,self.temp_score,self.current.total_score))
            self.choice()
            
            
    def scores(self):
        self.temp_score=0
        if self.current.total_score >=20:
            print("GAME OVER, {} wins with {} points!".format(self.current.name,self.current.total_score))
            sys.exit()
        
        else:
            if self.pcount==self.num_players-1:
                self.pcount=0
                self.current=self.players[self.pcount]
                print('{}\'s turn!'.format(self.current.name))
                self.go()
            
            else:
                while self.pcount <= self.num_players:
                    self.pcount+=1
                    self.current=self.players[self.pcount]
                    print('{}\'s turn!'.format(self.current.name))
                    self.go()
                    
    def choice(self):
        result = self.current.r_or_h()
        
        if result == 'roll':
            self.go()
        elif result == 'hold':
            self.current.total_score+=self.temp_score
            self.scores()
        else:
            self.choice()
                
Pig = Game(3)

if __name__ == '__main__':
    Pig



