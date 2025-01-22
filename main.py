# A Mech themed football manager style game

# Pilots
class Pilot:
    def __init__(self,name,skill,mech,salary):
        self.name=name
        self.skill=skill
        self.mech=mech
        self.salary=salary

    def __str__(self):
        return f'{self.name}\nSkill: {self.skill}\nMech: {self.mech}\nSalary: {self.salary}\n'

class Mech:
    def __init__(self,name,durability,power,speed,cost):
        self.name=name
        self.durability=durability
        self.power=power,
        self.speed=speed
        self.cost=cost
        
    def __str__(self):
        return f'{self.name}\nDurability: {self.durability}\nPower: {self.power}\nSpeed: {self.speed}\nCost: ${self.cost}'
    
Pilots={
    'Alice':Pilot('Alice',8,'coyote',80),
    'Brent':Pilot('Brent',7,'anteater',65),
    'Connor':Pilot('Connor',6,'badger',60),
    'David':Pilot('David',7,'coyote',70),
}

Mechs={
    'anteater':{
        'durability':7,
        'power':4,
        'speed':3,
    },
    'badger':{
        'durability':7,
        'power':5,
        'speed':5
    },
    'coyote':{
        'durability':5,
        'speed':6,
        'power':8,
        'cost':50
    }
}
Teams={
    'Alpha Team':{
        'pilots':['Alice','Connor'],
        'wins':0,
        'losses':0,
        'funds':200
    },
    'Bravo Team':{
        'pilots':['Brent','David'],
        'winse':0,
        'losses':0,
        'funds':200
    }
}

def combat(t1,t2):
    pass

def mainloop():
    pass

mainloop()