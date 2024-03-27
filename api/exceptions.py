from rest_framework.exceptions import APIException

class keyErrorException(APIException):

    status_code=400
    default_detail="Invalid request body. Please Try again"

class noObjectException(APIException):

    def __init__(self, detail=None, code=None,model=None):
        # use for authentication exceptions
        if model:
            self.detail = f"Requested {model} not found in the library"
            self.status_code = 404
        else:
            self.detail = "Invalid Credentials"
            self.status_code = 401

class noTokenException(APIException):
    
    def __init__(self,token, detail=None, code=None):
        self.status_code = 400
        if token=="JWT":
            self.detail = f"No {token} token in the session or expired. Kindly login again"
        else:
            self.detail = f"No {token} token Provided..Bad request"

class invalidTokenException(APIException):
    status_code = 401
    default_detail = "Invalid Token"

class invalidRoleException(APIException):

    def __init__(self,detail=None, code=None):
        self.status_code = 403
        self.detail = f"You dont possess enough permissions for this action"
        
        
    