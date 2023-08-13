from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi_cache.decorator import cache

from ..auth.base_config import current_user

from .tasks import send_email_report_dashboard

router = APIRouter(prefix="/report")


@router.get("/dashboard")
@cache(expire=60)
def get_dashboard_report(user=Depends(current_user)):
    # 600 ms - Задача выполняется воркером Celery в отдельном процессе
    send_email_report_dashboard.delay(user.username)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
