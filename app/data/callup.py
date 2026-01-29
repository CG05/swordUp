from app.models.weapon import Weapon, EnhanceTier, WeaponCategory, Level, Chance
from app.data.weapons import WEAPONS
from app.data.levels import LEVELS, CHANCES
# from app.data.power_table

def enhance_tier(level: int) -> EnhanceTier:
    if level <= 10:
        return EnhanceTier.LOW
    if level <= 17:
        return EnhanceTier.MID
    if level <= 21:
        return EnhanceTier.HIGH
    if level <= 23:
        return EnhanceTier.LEGEND
    return EnhanceTier.MYTH

    
def weapon(key: str) -> Weapon:
    return WEAPONS[key]
    
def level(level: int) -> Level:
    return LEVELS[level]

def add_chance(level: int, tier: EnhanceTier) -> float:
    add = 0.00
    if tier == EnhanceTier.LOW:
        add = (level-10) * 0.05
    elif tier == EnhanceTier.MID:
        add = (level-17) * 0.07
    return add

def enhance_chance(category: WeaponCategory, level: int) -> Chance:
    tier = enhance_tier(level)
    chance = CHANCES[category][tier]
    if category == WeaponCategory.NORMAL:
        add = add_chance(level, tier)
        chance.up += add
    return chance