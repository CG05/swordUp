from app.models.weapon import Weapon, WeaponCategory

WEAPONS = {
    # ===== 일반무기 =====
    "sword1": Weapon("sword1", "한손검", WeaponCategory.NORMAL, 25),
    "sword2": Weapon("sword2", "양손검", WeaponCategory.NORMAL, 25),
    "sword3": Weapon("sword3", "쌍검", WeaponCategory.NORMAL, 25),
    "dagger1": Weapon("dagger1", "한손단검", WeaponCategory.NORMAL, 25),
    "dagger2": Weapon("dagger2", "쌍단검", WeaponCategory.NORMAL, 25),
    "magic_sword": Weapon("magic_sword", "마법검", WeaponCategory.NORMAL, 25),
    "spear": Weapon("spear", "창", WeaponCategory.NORMAL, 25),
    "axe": Weapon("axe", "도끼", WeaponCategory.NORMAL, 25),
    "club": Weapon("club", "몽둥이", WeaponCategory.NORMAL, 25),
    "hammer": Weapon("hammer", "망치", WeaponCategory.NORMAL, 25),
    "bow": Weapon("bow", "활", WeaponCategory.NORMAL, 25),
    "crossbow": Weapon("crossbow", "석궁", WeaponCategory.NORMAL, 25),
    "wand": Weapon("wand", "완드", WeaponCategory.NORMAL, 25),
    "staff": Weapon("staff", "스태프", WeaponCategory.NORMAL, 25),
    "knuckle": Weapon("knuckle", "너클", WeaponCategory.NORMAL, 25),
    "claw": Weapon("claw", "클로", WeaponCategory.NORMAL, 25),

    # ===== 특수무기 =====
    "branch": Weapon("branch", "나뭇가지", WeaponCategory.SPECIAL, 25),
    "frying_pan": Weapon("frying_pan", "프라이팬", WeaponCategory.SPECIAL, 25),
    "kitchen_knife": Weapon("kitchen_knife", "식칼", WeaponCategory.SPECIAL, 25),
    "beer_bottle": Weapon("beer_bottle", "맥주병", WeaponCategory.SPECIAL, 25),
    "keyboard": Weapon("keyboard", "키보드", WeaponCategory.SPECIAL, 25),
    "spray": Weapon("spray", "스프레이", WeaponCategory.SPECIAL, 25),

    # ===== 유물무기 =====
    "excalibur": Weapon("excalibur", "엑스칼리버", WeaponCategory.RELIC, 25),
    "ganjiang_moye": Weapon("ganjiang_moye", "간장막야", WeaponCategory.RELIC, 25),
    "gungnir": Weapon("gungnir", "궁니르", WeaponCategory.RELIC, 25),
    "ruyi_bang": Weapon("ruyi_bang", "여의봉", WeaponCategory.RELIC, 25),
    "merlin_grimoire": Weapon("merlin_grimoire", "멀린의 마도서", WeaponCategory.RELIC, 25),
    "brahmastra": Weapon("brahmastra", "브라흐마스트라", WeaponCategory.RELIC, 25),
}