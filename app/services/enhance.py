import random
from app.models.weapon import Weapon, EnhanceTier, WeaponCategory, get_enhance_chance, get_enhance_tier, Chance
from app.storage.redis import load_user, save_user

def roll(chance: Chance, add: float) -> str:
    r = random.random()
    acc = 0.00

    acc += (chance.up + add)
    if r < acc:
        return "up"

    acc += chance.down
    if r < acc:
        return "down"

    acc += chance.crash
    if r < acc:
        return "crash"

    return "stay"

def add_chance(level: int, tier: EnhanceTier) -> float:
    add = 0.00
    if tier == EnhanceTier.LOW:
        add = (level-10) * 0.05
    elif tier == EnhanceTier.MID:
        add = (level-17) * 0.07
    return add
        

def enhance_weapon(user_id: str) -> str:
    
    # 1. 무기 정보
    category = weapon.category
    level = weapon.level
    tier = get_enhance_tier(level)
    add = 0.00
    if category == WeaponCategory.NORMAL:
        add = add_chance(level, tier)

    # 2. 확률 판정
    roll = roll(get_enhance_chance(category, tier), add)
    
    msg = "강화"

    if roll == "up":
        msg += "성공!!!"
        
    elif roll == "down":
        msg += "실패..."
    elif roll == "crash":
        msg == "강화가 실패하여 파괴되었습니다..."
    elif roll == "stay":
        msg += "유지."

