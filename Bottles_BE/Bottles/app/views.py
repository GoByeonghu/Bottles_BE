from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import Users
from app.serializers import UsersSerializer,UsersSerializer_SignUp

@csrf_exempt
def user_list(request):
    """
    List all users, or create a new user.
    only for test
    """

    #return all users data
    if request.method == 'GET':
        all_users = Users.objects.all()
        serializer = UsersSerializer(all_users, many=True)
        return JsonResponse(serializer.data, safe=False)

#존재하는 id인지 확인
def isExist(Model, target):
    return Model.objects.filter(id=target).exists()

#회원가입
class SignupView(APIView):
    def post(self, request):
        print(1)
        #아이디 중복 검사
        if(isExist(Users, request.data['id'])):
            return Response({ "error": "already exist id"},status=409)
        #회원정보저장
        print(2)
        #data = JSONParser().parse(request)
        print(3)
        serializer = UsersSerializer_SignUp(data=request.data)
        print(4)
        if serializer.is_valid():
            serializer.save()
            return Response({"register successfully"},status=200)
        
        #need to fix
        else:
            return Response({"error..."},status=500)

        """
        #회원정보 저장    
        user = Users.objects.create_user(username=request.data['id'], password=request.data['pw'])
        users = Users(user=user, is_student=request.data['is_student'] , name=request.data['name'], email=request.data['email'], school=request.data['school'], department=request.data['department'])      
        user.save()
        users.save()
        """