from fastapi import APIRouter
from pydantic import BaseModel
from app.storage.redis import load_user
import app.data.callup as data_callup
from app.services.enhance import enhance_weapon
import json

router = APIRouter()

class User(BaseModel):
    id: str

class UserRequest(BaseModel):
    user: User
    utterance: str

class KakaoRequest(BaseModel):
    userRequest: UserRequest


# 오류 처리 포함, 간단한 docker 서버 내부 로깅
@router.post("/kakao")
async def kakao_webhook(req: KakaoRequest):
    user_id = req.userRequest.user.id
    text = req.userRequest.utterance.strip()
    try:
        state = load_user(user_id)
    except Exception as e:
        print(f"Error loading user {user_id}: {e}")
        return {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "사용자 정보를 불러오는 중 오류가 발생했습니다. 다시 시도해주세요."
                        }
                    }
                ]
            }
        }

    if text == "/강화":
        result_text = enhance_weapon(user_id)
        print(f"User {user_id} 강화 결과: {result_text}")
        return 강화응답(result_text)

    elif text == "/프로필":
        print(f"User {user_id} 요청: 프로필")
        return 프로필응답(user_id)

    else:
        print(f"User {user_id} 알 수 없는 명령어: {text}")
        return {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "알 수 없는 명령어입니다. /강화 또는 /프로필을 사용하세요."
                        }
                    }
                ]
            }
        }
    

def 강화응답(result_text: str):
    #리턴 메시지 헤더, 바디 정의
    header = {
        "version": "2.0",
        "template": {
            "outputs": [],
            "quickReplies": []
        }
    }
    body = header["template"]
    body["outputs"].append({
        "simpleText": {
            "text": result_text
        }
    })
    body["quickReplies"].append({
        "label": "⚒️ 다시 강화",
        "action": "message",
        "messageText": "/강화"
    })
    return header

def 프로필응답(user_id: str):
    state = load_user(user_id)
    weapon = data_callup.weapon(state["weapon_key"])
    level = data_callup.level(state["level"])
    profile_text = (
        f"🗡️ 무기: +{level.key} {level.name} {weapon.name}\n"
    )
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": profile_text
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "⚒️ 강화하기",
                    "action": "message",
                    "messageText": "/강화"
                }
            ]
        }
    }
