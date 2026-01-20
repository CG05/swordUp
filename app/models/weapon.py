from dataclasses import dataclass
from enum import Enum
from app.data import weapons, grades, power_table

@dataclass(frozen=True)
class WeaponCategory(str, Enum):
    NORMAL = "일반무기"
    SPECIAL = "특수무기"
    RELIC = "유물무기"

@dataclass(frozen=True)
class EnhanceTier(str, Enum):
    LOW = "low"        # +0 ~ +10
    MID = "mid"        # +10 ~ +17
    HIGH = "high"      # +18 ~ +21
    LEGEND = "legend"  # +22 ~ +23
    MYTH = "myth"      # +24 ~ +25

@dataclass(frozen=True)
class Weapon:
    key: str
    name: str
    category: str
    max_grade: int

@dataclass(frozen=True)
class Grade:
    key: int
    name: str
    
@dataclass(frozen=True)
class Chance:
    key: str
    up: float
    down: float
    crash: float
    revive: int
    
def get_enhance_tier(level: int) -> EnhanceTier:
    if level <= 10:
        return EnhanceTier.LOW
    if level <= 17:
        return EnhanceTier.MID
    if level <= 21:
        return EnhanceTier.HIGH
    if level <= 23:
        return EnhanceTier.LEGEND
    return EnhanceTier.MYTH

def get_enhance_chance(category: WeaponCategory, tier: EnhanceTier) -> Chance:
    return grades.CHANCES[category][tier]
    
def get_weapon(key: str) -> Weapon:
    return weapons.WEAPONS[key]
    
def get_grade(grade: int) -> Grade:
    return grades.GRADES[grade]


