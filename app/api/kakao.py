from fastapi import APIRouter
from pydantic import BaseModel
from app.storage.redis import load_user
import app.data.callup as data_callup
from app.services.enhance import enhance_weapon

router = APIRouter()

class User(BaseModel):
    id: str

class UserRequest(BaseModel):
    user: User
    utterance: str

class KakaoRequest(BaseModel):
    userRequest: UserRequest


@router.post("/kakao")
async def kakao_webhook(req: KakaoRequest):
    user_id = req.userRequest.user.id
    text = req.userRequest.utterance.strip()

    if text == "/강화":
        result_text = enhance_weapon(user_id)
        return 강화응답(result_text)

    elif text == "/프로필":
        return 프로필응답(user_id)

    else:
        return
    

def 강화응답(result_text: str):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": result_text
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "⚒️ 다시 강화",
                    "action": "message",
                    "messageText": "/강화"
                }
            ]
        }
    }

def 프로필응답(user_id: str):
    state = load_user(user_id)
    weapon = data_callup.weapon(state["weapon_key"])
    level = data_callup.level(state["level"])
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"+{level.key} {level.name} {weapon.name} 보유중"
                    }
                }
            ]
        }
    }
