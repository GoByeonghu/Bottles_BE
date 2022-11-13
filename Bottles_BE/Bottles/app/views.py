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


#회원가입
class SignupView(APIView):
    def post(self, request):
        #아이디 중복 검사
        if(Users.objects.filter(id=request.data['id']).exists()):
            return Response({ "error": "already exist id"},status=409)
        #이메일 중복 검사
        if(Users.objects.filter(email=request.data['email']).exists()):
            return Response({ "error": "already exist email"},status=409)

        #렝스검사
        #https://hashcode.co.kr/questions/8710/%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94-%EC%9E%A5%EA%B3%A0-is_valid%EC%9D%98-%EB%8F%99%EC%9E%91%EB%B0%A9%EC%8B%9D%EC%9D%B4-%EA%B6%81%EA%B8%88%ED%95%A9%EB%8B%88%EB%8B%A4

        #회원정보저장
        #data = JSONParser().parse(request)
        serializer = UsersSerializer_SignUp(data=request.data)  
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