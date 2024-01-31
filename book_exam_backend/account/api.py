from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from .forms import SignupForm
from django.contrib.auth.forms import PasswordChangeForm

# get แสดงข้อมูล post สร้างข้อมูลใหม่ delete ลบ put อัพเดตข้อมูล
# model form api url


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = "success"

    form = SignupForm(
        {
            "username": data.get("username"),
            "email": data.get("email"),
            "firstname": data.get("firstname"),
            "lastname": data.get("lastname"),
            "role": data.get("role"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
            "prefix": data.get("prefix"),
        }
    )

    if form.is_valid():
        form.save()

    else:
        print(form.errors)
        message = "error"
    return JsonResponse({"message": message})

@api_view(["GET"])
def userInfo(request):
    return JsonResponse({
        "id": request.user.id,
        "username": request.user.username,
        "firstname": request.user.firstname,
        "lastname": request.user.lastname,
        "email": request.user.email,
        "role": request.user.role,
        "prefix": request.user.prefix,
    })
    
# change Password
@api_view(["POST"])
def changePassword(request):
    user = request.user

    form = PasswordChangeForm(data=request.POST, user=user)

    if form.is_valid():
        form.save()

        return JsonResponse({"message": "success"})
    else:
        return JsonResponse({"message": form.errors.as_json()}, safe=False)
