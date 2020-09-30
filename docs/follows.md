# Likes

signed-in users can follow and unfollow other users.

## **follow user**
----
  follow the user with the provided `id`.

* **URL**

  `/api/follows`

* **Method:**

  `POST`

* **Request Body Params**

| parameter          | required           | description                             |
| :----------------: | :----------------: | :-------------------------------------- |
| `user_id`[integer] | :heavy_check_mark: | the user_id for the user who want to follow another user |
| `followed_user_id`[integer] | :heavy_check_mark: | the user_id of the user to be followed |

* **Success Response:**

  * **Code:** 201 Created<br />
    **Content:** 
    ``` javascript
      {
        "detail": "successful"
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
            "detail": "username must be a valid existing user's username",
            "param": "username"
    ]
}
```

  OR

  * **Code:** 422 Unprocessable Entity<br />
    **Content:**
    ``` javascript
    {
    "detail": "missing or invalid info"
}
```
  OR

  * **Code:** 403 Forbidden<br />
    **Content:**
    ``` javascript
    {
    "detail": "Authrization required"
}
```

* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/follows",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : { 
	"user_id" : "1",
	"followed_user_id" : "3",
  },
  type : "POST",
  success : function(r) {
    console.log(r);
  }
});
```


* **Notes:**

  request must include the JWT token in the `Authorization` header, not including the token would result in an HTTP response code of 401 Unauthorized. a non-401 fail response contains an array of errors, if it doesn't that means you are trying to follow yourself or a user you're already following.

  ## **unfollow user**
----
  unfollow the user with the provided `user_follow table id`.

* **URL**

  `/api/follows/{id}`

* **Method:**

  `DELETE`

* **Request Body Params**


* **Success Response:**

  * **Code:** 204 NOT CONTENT<br />
    **Content:** 
    
 
* **Error Response:**

    **Content:** 
    ``` javascript

  OR

  * **Code:** 401 Unauthorized<br />
    **Content:**
    ``` javascript
    {
    "detail": "Authrization required"
}
```

* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/follows/5",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : { 
  },
  type : "DELETE",
  success : function(r) {
    console.log(r);
  }
});
```


* **Notes:**

  request must include the JWT token in the `Authorization` header, not including the token would result in an HTTP response code of 401 Unauthorized. a non-401 fail response contains an array of errors, if it doesn't that means you are trying to unfollow a user you're not following.
