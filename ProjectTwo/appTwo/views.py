from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from appTwo.models import ItemsList, UsersList,HotelsList
from appTwo.forms import UploadImageForm, SearchInfoForm,UserForm,NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from rest_framework import status
from appTwo.serializers import ItemSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

def uploadFile(request): #Function to upload an image file from the user and store it in database
    form = UploadImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            uploaded_img = form.save(commit=False)
            uploaded_img.image_data = form.cleaned_data['image'].file.read()
            uploaded_img.save()
            return redirect('/')
        else:
            form = UploadImageForm()
    return render(request, 'appTwo/upload.html', {'form': form})

def index(request):
    return render(request,'appTwo/index.html')

@api_view(['POST',])   
@permission_classes((IsAuthenticated,))
def searchInfo(request):# Function for Hotel details display when given owner name
    form = SearchInfoForm(request.POST, request.FILES)
    if request.method == 'POST':
        search_name= request.POST.get('textfield', None)
        try:
            user_id = UsersList.objects.only('person_id').get(person_firstname=search_name).person_id
            owner_list = HotelsList.objects.get(owner_id = user_id)
            detail_dict={"details":owner_list}
            return render(request,'appTwo/search.html',context=detail_dict)
        except HotelsList.DoesNotExist:
            return HttpResponse("no such user with that name")  
    else:
        return render(request,'appTwo/search.html',{'form': form})

def create(request): # Function for creating of new record in UsersList model _ CRUD Operations
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
                form.save()
                # token = Token.objects.create(user=user) 
                # print(token.key)
                return redirect('/read')
    else:  
        form = UserForm()  
    return render(request,'appTwo/createuser.html',{'form':form})  

# def token_request(request):
#     if user_requested_token() and token_request_is_warranted():
#         new_token = Token.objects.create(user=request.user)

def read(request): #Function to display the records of users- CRUD Operation
    # for user in UsersList.objects.all():
    #     print(user.person_id)
    #     Token.objects.get_or_create(user=user.person_id)
    user_list = UsersList.objects.all()
    user_dict = {"users":user_list}
    return render(request,'appTwo/users.html',context=user_dict)

def edit(request): # Function to display the records of user for updating the record- CRUD Operation
     if request.method == 'POST':
        name= request.POST.get('textfield', None)
        user = UsersList.objects.get(person_firstname=name)  
        return render(request,'appTwo/edit.html', {'user':user}) 
     else:
        return render(request,'appTwo/index.html')
 

def update(request, name):  # Function to update a record- CRUD Operation
    user = UsersList.objects.get(person_firstname=name) 
    form = UserForm(request.POST,instance=user)
    if form.is_valid():  
        form.save()  
        return redirect("/read")  
    return render(request, 'appTwo/edit.html', {'user': user})  

def delete(request, name):   # Function to delete a record- CRUD Operation
    user = UsersList.objects.get(person_firstname=name)  
    user.delete()  
    return redirect("/read")  

def register(request):  # Function for registering new user 
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
            # token=Token.objects.get(user=user).key
			messages.success(request, "Registration successful." )
			return redirect('appTwo/index.html')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,'appTwo/register.html', {"form":form})

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


@csrf_exempt
def item_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        items = ItemsList.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def item_detail(request, pk):
    try:
        item = ItemsList.objects.get(item_name=pk)
    except ItemsList.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)