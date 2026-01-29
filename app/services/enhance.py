import random
from app.models.weapon import Chance
import app.data.callup as data_callup
from app.storage.redis import load_user, save_user

def roll(chance: Chance) -> str:
    r = random.random()
    acc = 0.00

    acc += chance.up
    if r < acc:
        return "up"

    acc += chance.down
    if r < acc:
        return "down"

    acc += chance.crash
    if r < acc:
        return "crash"

    return "stay"
        

def enhance_weapon(user_id: str) -> str:
    state = load_user(user_id)
    weapon = (state["weapon_key"])
    # 1. 무기 정보
    category = weapon.category
    level = state["level"]

    # 2. 확률 판정
    roll = roll(data_callup.enhance_chance(category, level))
    
    msg = "강화"

    if roll == "up":
        state["level"] += 1
        save_user(user_id, state)
        msg += "성공!!!"
        
    elif roll == "down":
        state["level"] -= 1
        save_user(user_id, state)
        msg += "실패..."
    elif roll == "crash":
        state["level"] = 0
        save_user(user_id, state)
        msg == "강화가 실패하여 파괴되었습니다..."
    elif roll == "stay":
        msg += "유지."

