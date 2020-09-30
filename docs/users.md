# Users accounts 

Guests can register or sign-in, signed-in users can update their info and settings or log-out.

## **register user**
----
  create a new account and set their `username`, `email` , `password1` and `password2` to the given arguments, a sucess response contains JWT for authorization.

* **URL**

  `/rest-auth/registration/`

* **Method:**

  `POST`

* **Request Body Params**

| parameter                 | required           | description                                                                                                                                                                                   |
| :-----------------------: | :----------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `username`[string]        | :heavy_check_mark: | used to login and as a display name on the website, must be between 4 to 15 characters long, can only contain alphanumerics, underscores and dashes, and must not be already in use</li></ul> |
| `email`   [string]        | :heavy_check_mark: | must be a valid email address and not already in use                                                                                                                                          |
| `password1` [string]       | :heavy_check_mark: | used to login, must be at least 8 characters long, include one lowercase character, one uppercase character, a number, and a special character                                                |
| `password2`[string] | :heavy_check_mark: | double checks that the entered password1 is the one really desired by the user, must match `password1`                                                                                          |

* **Success Response:**

  * **Code:** 201 Created<br />
    **Content:** 
    ``` javascript
      {
        "detail": "successful",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjkzLCJpYXQiOjE1MjE2NDA4MjQsImV4cCI6MTUyMTY1MTYyNH0.KaJSnxnECC1S-amUhyjM-sifNCwksY_kAELFU71LCyg" 
        "user" : [user data]
      }
    ```
 
* **Error Response:**

  * **Code:** 422 Unprocessable Entity<br />
    **Content:** 
    ``` javascript
{
    "detail": "missing or invalid info",
    "errors": [
        {
            "detail": "username must be between 4 to 15 characters long, and can only contain alphanumerics, underscores and dashes.",
            "param": "username"
        },
        {
            "detail": "e-mail must be a valid e-mail address.",
            "param": "email"
        },
        {
            "detail": "password must be at least 8 characters long, and include one lowercase character, one uppercase character, a number, and a special character.",
            "param": "password"
        },
        {
            "detail": "passwords must match",
            "param": "confirmpassword"
        }
    ]
}
```

  OR

  * **Code:** 422 Unprocessable Entity<br />
    **Content:** 
    ``` javascript
{
    "detail": "missing or invalid info",
    "errors": [
        {
            "detail": "username must be between 4 to 15 characters long, and can only contain alphanumerics, underscores and dashes.",
            "param": "username"
        },
        {
            "detail": "e-mail must be a valid e-mail address.",
            "param": "email"
        }
    ]
}
```

* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/register",
  headers: {
        'Content-Type':'application/json'
    },
  dataType: "json",
  data : { 
	"username" : "john",
	"password1" : "Aa@123456",
	"password2" : "Aa@123456",
	"email" : "test@email.com"
  },
  type : "POST",
  success : function(r) {
    console.log(r);
  }
});
```


* **Notes:**

  a success response will always contain a JWT that must be saved in localStorage, this JWT must be included in the `Authorization` header in every request sent afterwards to authenticate the user, failing to do so will result in an HTTP response of code "401 Unauthorized", check the <a href="#/users?id=update-user-info" class="anchor">"update user info"</a> section for an example.

## **Sign in**
----
  authenticate the guest by checking the entered `username` and `password`, a sucess response contains JWT for authorization.

* **URL**

  `/rest-auth/login/`

* **Method:**

  `POST`
  
* **Request Body Params**

| parameter          | required           | description                        |
| :----------------: | :----------------: | :--------------------------------- |
| `username`[string] | :heavy_check_mark: | username used during registeration |
| `password`[string] | :heavy_check_mark: | password used during registeration |

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:**
    ``` javascript
      {
        "detail": "successful",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjkzLCJpYXQiOjE1MjE2NDA4MjQsImV4cCI6MTUyMTY1MTYyNH0.KaJSnxnECC1S-amUhyjM-sifNCwksY_kAELFU71LCyg" 
        "user" : [user data]
      }
    ```
 
* **Error Response:**

  * **Code:** 422 Unprocessable Entity<br />
    **Content:**
    ``` javascript
      {
        "detail": "invalid username or password"
      }
    ```
 


* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/login",
  headers: {
        'Content-Type':'application/json'
    },
  dataType: "json",
  data : { 
	"username" : "john",
	"password" : "Aa@123456"
  },
  type : "POST",
  success : function(r) {
    console.log(r);
  }
});
```

* **Notes:**

    a success response will always contain a JWT that must be saved in localStorage, this JWT must be included in the `Authorization` header in every request sent afterwards to authenticate the user, failing to do so will result in an HTTP response of code "401 Unauthorized", check the <a href="#/users?id=update-user-info" class="anchor">"update user info"</a> section for an example.


## **update user info**
----
  update the user's `username`, `email`, `firstname`, `lastname`, `issuperuser` or `isstaff` .

* **URL**

`/api/users/{id}`

* **Method:**
  
  `PATCH`

* **Request Body Params**

  
| parameter                      | required | description                                                                                                                                               |
| :----------------------------: | :------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `username`[string]          |          | desired new username, must be between 4 to 15 characters long, and can only contain alphanumerics, underscores and dashes, and must not be already in use |
| `email`[string]             |          | desired new email address, must be a valid email address and not already in use                                                                           |
| `firstname`[string]          |          | desired new firstname |
| `lastname`[string] |          |  desired new lastname       |
| `issuperuser`[integer]               |          | desired new avatar, must be 0 or 1                                                                                                |
| `isstaff`[integer]                  |          | desired new user bio, must be 0 or 1                                                                                                          |

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:**
    ``` javascript
    {
    "detail": "successful",
    "user": {
        "username": "hossain-mohammed",
        "email": "newemail@test.com",
        "firstname": "Hossain",
        "lastname": "Mohammed",
        "issuperuser": false,
        "isstaff": true,
    }
}
```
 
* **Error Response:**

  * **Code:** 422 Unprocessable Entity <br />
      **Content:**
      ``` javascript
      {
      "detail": "missing or invalid info",
      "errors": [
        {
              "detail": "this email is already in use.",
              "param": "newemail"
          },
          {
              "detail": "Invalid value",
              "param": "isstaff"
          }
      ]
  }
  ```
OR

  * **Code:** 422 Unprocessable Entity<br />
    **Content:**
    ``` javascript
    {
    "detail": "missing or invalid info",
}
```
OR

  * **Code:** 401 Unauthorized<br />
    **Content:**
    ``` javascript
    {
    "detail": "auth failed",
}
```

* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/users",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : { 
	"username" : "mahmoud_ahmed",
	"firstname" : "Mahmoud"
  },
  type : "PATCH",
  success : function(r) {
    console.log(r);
  }
});
```

## **get all users data**
----
  list all users data.

* **URL**

`/api/users`

* **Method:**
  
  `GET`


* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:**
    ``` javascript
    {
    "detail": "successful",
    "users": {
        [user1 data],
        [user2 data],
        ........
    }
}
```
 
* **Error Response:**

  * **Code:** 401 Unauthorized<br />
    **Content:**
    ``` javascript
    {
    "status" : "403"
    "detail": "Authorization required",
}
```

* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/users",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : { },
  type : "GET",
  success : function(r) {
    console.log(r);
  }
});
```

## **get user data**
----
lest user data by its id

* **URL**

`/api/users/{id}`

* **Method:**
  
  `GET`


* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:**
    ``` javascript
    {
    "detail": "successful",
    "users": {
        user1 data
    }
}
```
 
* **Error Response:**

  

  * **Code:** 401 Unauthorized<br />
    **Content:**
    ``` javascript
    {
    "status" : "403"
    "detail": "Authorization required",
}
```

* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/users/1",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : { },
  type : "GET",
  success : function(r) {
    console.log(r);
  }
});
```
## **delete user**
----
delete user by id
* **URL**

`/api/users/{id}`

* **Method:**
  
  `DELETE`


* **Success Response:**
  
  * **Code:** 204 NOT CONTENT <br />
    **Content:**
    
 
* **Error Response:**

  

  * **Code:** 401 Unauthorized<br />
    **Content:**
    ``` javascript
    {
    "status" : "403"
    "detail": "Authorization required",
}
```

* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/users/1",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : { },
  type : "GET",
  success : function(r) {
    console.log(r);
  }
});
```
* **Notes:**

  a request must only include the fields that the user wants to update and must include the JWT token in the `Authorization` header, 
  not including the token would result in an HTTP response code of 403 Forbidden. a non-401 fail response contains an array of errors, 
  if it doesn't that means no fields were sent in the request body. a success response contains the updated fields. 