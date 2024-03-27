## Personal Library 

### Set-Up

Clone the repository and Enter into the directory  

Create an virtual environment  
```bash
python -m venv .venv
```
   
Activate the virtual environment  
```bash
. .venv/bin/activate
```

If you want to prefer global installations, you can ignore the above  

Install the dependencies  
```bash
pip install -r requirements.txt
```

Apply migrations and migrate to the database  
```bash 
python manage.py makemigrations  
python manage.py migrate  
```

Run the server
```bash
python manage.py runserver
```

**Now the server is up and serving on port 8000**

### Usage

#### Routes 

*All routes are extended from the (/api/v1) path*
  
**/user/register/ - Register Route  for New user**  
**/user/login/    - Login Route for Registered User**    
**/user/logout/   - Logout Route for current Logged User**   
**/books/         - Listing and Adding Books for the Active User**  
**/books/$isbn/   - Retrieve,Update,Delete particular book from library for Active User**    

*Debug is set to True, So you can see all available routes in / route*

#### Guide

Hit Register Route and register the user : **POST**  
Requirements - Username,Password,Confirm_Password  
   
Login with your credentials on login route : **POST**  
Requirements - Username,Password  

Add a book in listing and add route : **POST**  
Requirements - Title,Author,ISBN,Publication_Date(Optional),Description(Optional)  

List all the books in user library : **GET**  

Retrieve,Update,Delete Route 
   
Retrieve **GET**  
Update   **PUT** : All requirements as Adding a book  
Delete   **DELETE** 


#### Tests

Tests are written with django Testcase for Major Views   

Run  
```bash
python manage.py test
```