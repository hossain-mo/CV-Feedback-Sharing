# Likes

signed-in users can like and unlike CVs.

## **post like**
----
  like the article with the provided `cv_id`.

* **URL**

  `/api/likes`

* **Method:**

  `POST`

* **Request Body Params**

| parameter             | required           | description                       |
| :-------------------: | :----------------: | :-------------------------------- |
| `user_id`[integer] | :heavy_check_mark: | the ID of the user who like |
| `cv_id`[integer]  | :heavy_check_mark: | the ID of the cv to be liked |

* **Success Response:**

  * **Code:** 201 Created<br />
    **Content:** 
    ``` javascript
      {
        "msg": "successful"
      }
    ```
 
* **Error Response:**

  * **Code:** 400 Bad Request<br />
    **Content:** 
    ``` javascript
  {
    "msg": "missing or invalid info",
    "errors": [
        {
            "msg": "cv id is missing or invalid.",
            "param": "cv_id"
    ]
        }
  }


  OR

  * **Code:** 403 Forbidden<br />
    **Content:**
    ``` javascript
    {
    "detail": "Authentication Required"
    }

* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/likes",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : { 
	"user_id" : 15,
	"cv_id" : 12
  },
  type : "POST",
  success : function(r) {
    console.log(r);
  }
});
```


* **Notes:**

  request must include the JWT token in the `Authorization` header, not including the token would result in an HTTP response code of 401 Unauthorized. a non-401 fail response contains an array of errors, if it doesn't that means this user has already liked this article.

  ## **delete like**
----
  unlike the already liked CV with provided `cv_like_id`.

* **URL**

  `/api/likes/{id}`

* **Method:**

  `DELETE`

* **Request Body Params**


* **Success Response:**

  * **Code:** 204 NOT CONTENT<br />
    **Content:** 
   
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST<br />
    **Content:** 
    ``` javascript
{
    "msg": "missing or invalid info",
    "errors": [
        {
            "msg": "CV id is missing or invalid."
    ]
}
```

  
  OR

  * **Code:** 403 Forbidden<br />
    **Content:**
    ``` javascript
    {
    "msg": "Authentication Required"
}
```

* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/likes/{236}",
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

  request must include the JWT token in the `Authorization` header, not including the token would result in an HTTP response code of 401 Unauthorized. a non-401 fail response contains an array of errors, if it doesn't that means this user hasn't liked this article before.
