from app.models.weapon import Level, WeaponCategory, EnhanceTier, Chance

LEVELS = {
    0: Level(0, "낡아버린"),
    1: Level(1, "이빠진"),
    2: Level(2, "금이간"),
    3: Level(3, "녹슨"),
    4: Level(4, "겨우 쓸만한"),
    5: Level(5, "정비된"),
    6: Level(6, "손에 익은"),
    7: Level(7, "균형잡힌"),
    8: Level(8, "단련된"),
    9: Level(9, "숙련자의"),
    10: Level(10, "정예의"),
    11: Level(11, "명성이 도는"),
    12: Level(12, "전투를 기억하는"),
    13: Level(13, "영혼이 스민"),
    14: Level(14, "전설의 문턱에 선"),
    15: Level(15, "전설적인"),
    16: Level(16, "영웅이 사용한"),
    17: Level(17, "신화에 기록된"),
    18: Level(18, "초월자의"),
    19: Level(19, "현실을 베는"),
    20: Level(20, "개념을 파괴하는"),
    21: Level(21, "법칙을 거스르는"),
    22: Level(22, "세계에 거부당한"),
    23: Level(23, "신들이 경계하는"),
    24: Level(24, "존재를 찢는"),
    25: Level(25, "이름조차 금기인"),
}

CHANCES = {
    WeaponCategory.NORMAL: {
        EnhanceTier.LOW: Chance(
            key="normal_low",
            up=0.55,
            down=0.00,
            crash=0.00,
            revive=0
        ),
        EnhanceTier.MID: Chance(
            key="normal_mid",
            up=0.34,
            down=0.00,
            crash=0.01,
            revive=0
        ),
        EnhanceTier.HIGH: Chance(
            key="normal_high",
            up=0.30,
            down=0.10,
            crash=0.03,
            revive=0
        ),
        EnhanceTier.LEGEND: Chance(
            key="normal_legend",
            up=0.15,
            down=0.20,
            crash=0.10,
            revive=12
        ),
        EnhanceTier.MYTH: Chance(
            key="normal_myth",
            up=0.15,
            down=0.30,
            crash=0.25,
            revive=18
        ),
    },

    WeaponCategory.SPECIAL: {
        EnhanceTier.LOW: Chance(
            key="special_low",
            up=0.35,
            down=0.00,
            crash=0.01,
            revive=0
        ),
        EnhanceTier.MID: Chance(
            key="special_mid",
            up=0.35,
            down=0.00,
            crash=0.05,
            revive=0
        ),
        EnhanceTier.HIGH: Chance(
            key="special_high",
            up=0.35,
            down=0.20,
            crash=0.15,
            revive=0
        ),
        EnhanceTier.LEGEND: Chance(
            key="special_legend",
            up=0.35,
            down=0.35,
            crash=0.25,
            revive=18
        ),
        EnhanceTier.MYTH: Chance(
            key="special_myth",
            up=0.35,
            down=0.25,
            crash=0.40,
            revive=21
        ),
    },

    WeaponCategory.RELIC: {
        EnhanceTier.LOW: Chance(
            key="relic_low",
            up=0.00,
            down=0.00,
            crash=0.00,
            revive=0
        ),
        EnhanceTier.MID: Chance(
            key="relic_mid",
            up=0.45,
            down=0.00,
            crash=0.10,
            revive=12
        ),
        EnhanceTier.HIGH: Chance(
            key="relic_high",
            up=0.25,
            down=0.10,
            crash=0.20,
            revive=18
        ),
        EnhanceTier.LEGEND: Chance(
            key="relic_legend",
            up=0.15,
            down=0.20,
            crash=0.30,
            revive=21
        ),
        EnhanceTier.MYTH: Chance(
            key="relic_myth",
            up=0.05,
            down=0.30,
            crash=0.40,
            revive=23
        ),
    },
}
