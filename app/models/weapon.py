from dataclasses import dataclass
from enum import Enum


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
    max_level: int

@dataclass(frozen=True)
class Level:
    key: int
    name: str
    
@dataclass(frozen=True)
class Chance:
    key: str
    up: float
    down: float
    crash: float
    revive: int
