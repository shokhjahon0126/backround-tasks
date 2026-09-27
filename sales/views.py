from django.http import request,response
from core.celery import app

from .tasks import long_task




def celery_view(request:request.HttpRequest)->response.JsonResponse:

    print("Calery ishga tushdi")
    long_task.delay(35)

    return response.JsonResponse(
        {"message":"succes"}
    )


def get_status(request: request.HttpRequest) -> response.JsonResponse:
    task_id = request.GET.get("task_id")

    if task_id:
        result = app.AsyncResult(task_id)

        return response.JsonResponse(
            data={
                "state":result.state,
                "info":result.info
            }
        )
    
    return response.JsonResponse({
        "message":"Kutib tur"
    })
