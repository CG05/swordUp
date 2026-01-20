def talk(result: dict) -> str:
    if not result["ok"]:
        return f"대장장이: {result['reason']}"

    if result["success"]:
        return f"대장장이: 강화 성공! +{result['after']}"

    return "대장장이: 실패했지만 무기는 버텼다."
