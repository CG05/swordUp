import random
from app.models.weapon import Chance
import app.data.callup as data_callup
from app.storage.redis import load_user, save_user

def roll(chance: Chance) -> str:
    r = random.random()
    acc = 0.00

    acc += chance.up
    print(f"Roll: {r}, Up threshold: {acc}")
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
    weapon = data_callup.weapon(state["weapon_key"])
    print(f"User {user_id} is enhancing weapon {weapon.key} at level {state['level']}")
    print(f"Weapon category: {weapon.category}")
    # 1. 무기 정보
    level = state["level"]

    # 2. 확률 판정
    roll_res = roll(data_callup.enhance_chance(weapon.category, level))
    
    msg = "강화"

    if roll_res == "up":
        state["level"] += 1
        save_user(user_id, state)
        msg += "성공!!!"
        
    elif roll_res == "down":
        state["level"] -= 1
        save_user(user_id, state)
        msg += "실패..."
        
    elif roll_res == "crash":
        state["level"] = 0
        save_user(user_id, state)
        msg == "강화가 실패하여 파괴되었습니다..."
        
    elif roll_res == "stay":
        msg += "유지."
        
    return msg
