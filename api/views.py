import datetime
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .exceptions import keyErrorException,noObjectException
from django.core.exceptions import ObjectDoesNotExist,ValidationError
from .utils import encode_jwt
from django.db import IntegrityError


@api_view(["POST"])
def RegisterHandler(request):
    
    """
    Register Handler for the User
    Requires Unique Username and Password
    """

    post_data  = request.data

    try:
        Username = post_data["Username"]
        Password = post_data["Password"]
        Confirm_password = post_data["Confirm_Password"]
    except KeyError:
        raise keyErrorException()
    
    if Password!=Confirm_password:
        return Response({"detail":"Passwords must match"},status=400)

    try:
        _user = User(username=Username)
        _user.set_password(Password)
        _user.save()

    except IntegrityError as e:
        return Response({"detail":str(e.__cause__)},status=400)
    except ValidationError as e:
        return Response({"detail":e.message},status=400)
    
    return Response({"Status":"Success","Message":"Registered_Successfully"},status=201)

@api_view(["POST"])
def LoginHandler(request):

    """
    Login Handler for the User
    Requires Username and Password
    """

    post_data = request.data

    try:
        username = post_data["Username"]
        password = post_data["Password"]
    except KeyError:
        raise keyErrorException()
        
    # get the user
    try:
        _user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        raise noObjectException()

    #try to match the passwords
    bool = _user.check_password(password)
    if not bool:
        raise noObjectException()

    token = encode_jwt({"ID":_user.pk})

    # set sessions 
    response = Response({"Status":"Success","Message":"Logged In successfuly"})
    response.set_cookie("jwt",token,expires=datetime.datetime.now()+datetime.timedelta(days=14))
    return response

@api_view(["GET"])
def LogoutHandler(request):

    """
    Logout Handler for Users
    Requires active session
    """

    response = Response({"Status":"Success","Message":"Logged out successfully"})
    response.set_cookie("jwt","",expires=datetime.datetime.now()+datetime.timedelta(days=-1))
    return response
