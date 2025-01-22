# A Mech themed football manager style game

# Pilots
class Pilot:
    def __init__(self,name,skill,mech,salary):
        self.name=name
        self.skill=skill
        self.mech=mech
        self.salary=salary

    def __str__(self):
        returnstring = f'{self.name}\nSkill: {self.skill}\n'
        returnstring += str(self.mech)
        returnstring += f'\nSalary: {self.salary}\n'
        return returnstring

class Mech:
    def __init__(self,name,durability,power,speed,cost):
        self.name=name
        self.durability=durability
        self.power=power,
        self.speed=speed
        self.cost=cost
        
    def __str__(self):
        return f'{self.name}\nDurability: {self.durability}\nPower: {self.power}\nSpeed: {self.speed}\nCost: ${self.cost}'

class Team:
    def __init__(self,name,pilots,wins,losses,funds):
        self.name=name
        self.pilots=pilots
        self.wins=wins
        self.losses=losses
        self.funds=funds       

    def __str__(self):
        returnstring=f'{self.name}\n\nWins: {self.wins}\nLosses: {self.losses}\nFunds: {self.funds}\n\nPilots\n'
        for pilot in self.pilots:
            returnstring+=str(pilot)+'\n'
        return returnstring
        
    
Pilots={
    'Alice':Pilot('Alice',8,'coyote',80),
    'Brent':Pilot('Brent',7,'anteater',65),
    'Connor':Pilot('Connor',6,'badger',60),
    'David':Pilot('David',7,'coyote',70),
}

Mechs={
    'anteater':Mech('anteater',7,4,3,140),
    'badger':Mech('badger',6,5,5,160),
    'coyote':Mech('coyote',5,6,7,180),
}
Teams={
    'Alpha Team':Team('Alpha Team',[Pilots['Alice'],Pilots['Connor']],0,0,200),
    'Bravo Team':Team('Bravo Team',[Pilots['David'],Pilots['Brent']],0,0,200),
}

def combat(t1,t2):
    return t1,t2

def mainloop():
    for team in Teams:
        print(Teams[team])

mainloop()
