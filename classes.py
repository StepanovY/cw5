from dataclasses import dataclass
from skills import Skill, FuryPunch, HardShot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name='Воин',
    max_health=60,
    max_stamina=30,
    attack=1.2,
    stamina=0.8,
    armor=1.2,
    skill=FuryPunch(),
)

ThiefClass = UnitClass(
    name='Вор',
    max_health=25,
    max_stamina=15,
    attack=0.9,
    stamina=1.2,
    armor=0.9,
    skill=HardShot(),
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
