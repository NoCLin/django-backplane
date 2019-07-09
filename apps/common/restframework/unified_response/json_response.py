from django.http import JsonResponse


def ok(data):
    return JsonResponse(data,
                        json_dumps_params={"ensure_ascii": False}
                        )


def error(error_type, data=None):
    return JsonResponse(
        {
            "code": error_type.code,
            "message": error_type.message,
            "data": data,
        },
        json_dumps_params={"ensure_ascii": False},
        status=error_type.status
    )
