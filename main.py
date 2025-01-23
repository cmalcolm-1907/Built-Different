# A Mech themed football manager style game

# Pilots
class Pilot:
    def __init__(self,name,team,skill,mech,salary):
        self.name=name
        self.team=team
        self.skill=skill
        self.mech=mech
        self.salary=salary

    def __str__(self):
        returnstring = f'{self.name}\nTeam: {self.team}\nSkill: {self.skill}\n'
        returnstring += str(self.mech)
        returnstring += f'\nSalary: {self.salary}'
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
        
    
Mechs={
    'anteater':Mech('anteater',7,4,3,140),
    'badger':Mech('badger',6,5,5,160),
    'coyote':Mech('coyote',5,6,7,180),
}

Pilots={
    'Alice':Pilot('Alice',None,8,Mechs['coyote'],80),
    'Brent':Pilot('Brent',None,7,Mechs['anteater'],65),
    'Connor':Pilot('Connor',None,6,Mechs['badger'],60),
    'David':Pilot('David',None,7,Mechs['coyote'],70),
}

Teams={
    'Alpha Team':Team('Alpha Team',[Pilots['Alice'],Pilots['Connor']],0,0,200),
    'Bravo Team':Team('Bravo Team',[Pilots['David'],Pilots['Brent']],0,0,200),
}

def Update_Teams(input_teams):
    for team in input_teams:
        for pilot in input_teams[team].pilots:
            pilot.team=team

def combat(t1,t2):
    fighters =[]
    for pilot in t1.pilots:
        fighters.append(pilot)
    for pilot in t2.pilots:
        fighters.append(pilot)
    sorted_fighters = sorted(fighters,key=lambda pilot: pilot.mech.speed*pilot.skill)
    return sorted_fighters

def mainloop():
    Update_Teams(Teams)
    ordered_list = combat(Teams['Alpha Team'],Teams['Bravo Team'])
    for fighter in ordered_list:
        print(fighter)
        print(f'Initiative: {fighter.skill*fighter.mech.speed}\n')

mainloop()
