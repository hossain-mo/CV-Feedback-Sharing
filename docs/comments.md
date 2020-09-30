# comments

Guests can read comments, signed-in users can read, create, update or delete comments.

## **create comment**
----
  create a new comment and set it's `file` and `user` to the given arguments, a sucess response contains the id of the created comment.

* **URL**

  `/api/comments`

* **Method:**

  `POST`

* **Request Body Params**

| parameter          | required           | description                                                                                                                                                                                         |
| :----------------: | :----------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cv`[integer]       | :heavy_check_mark: | cv_id                                                                                                        |
| `user`[intger]     | :heavy_check_mark: | user who upload who's comment                                                                                                           |
| `content`[string]     | :heavy_check_mark: | your comment                                                                                                           |

* **Success Response:**

  * **Code:** 201 Created<br />
    **Content:** 
    ``` javascript
      {
        "msg": "successful",
        "comment": {
          id:1,
          cv:"Hossain_Mohammed.pdf",
          user:"ahmed"
        } 
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
                  "msg": "body can not be empty",
                  "param": "body"
              },
              {
                  "msg": "date must be a valid date in the format of YYYY-MM-DD",
                  "param": "date"
              }
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
  url: "/api/comments",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : {
	"cv": "2",
	"user" :5,
	"content" :"Nice CV!"
	
},
  type : "POST",
  success : function(r) {
    console.log(r);
  }
});
```

* **Notes:**

  request must include the JWT token in the `Authorization` header, not including the token would result in an HTTP response code of 401 Unauthorized, a success response will always contain the id of the comment, you can request the comment using this id, check the <a href="#/comments?id=get-single-comment" class="anchor">"get single comment"</a> section for an example.


## **update comment**
----
  update an existing personal comment's `file`.

* **URL**

  `/api/comments/:id`

* **Method:**

  `PATCH`

* **Request Body Params**

| parameter              | required           | description                                                                                                                                                                                             |
| :--------------------: | :----------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `content`[string]           | :heavy_check_mark: | the new comment content that you would like to update                                                                                                                                            |

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:** 
    ``` javascript
      {
          "msg": "successful",
          "comment": {
              "content": "content"
          }
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
                  "msg": "comment id is missing or invalid",
                  "param": "comment_id"
              },
              {
                  "msg": "title must not be empty and can not be more than 50 characters long",
                  "param": "newtitle"
              }
          ]
      }
    ```
OR

  * **Code:** 401 Unauthorized<br />
    **Content:**
    ``` javascript
    {
    "msg": "Authentication Required"
}
```


* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/comments/5",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : {
	"content": "You should do something else",
},
  type : "PATCH",
  success : function(r) {
    console.log(r);
  }
});
```


* **Notes:**

  a request must only include the fields that the user wants to update and must include the JWT token in the `Authorization` header, not including the token would result in an HTTP response code of 401 Unauthorized. a non-401 fail response contains an array of errors, if it doesn't that means no fields were sent in the request body, trying to update an comment that was created by someone else would result in an HTTP response code of 401 Unauthorized, success response contains the updated fields.

## **get all comments**
----
  get all the info of a all comments.

* **URL**

  `/api/comments/`

* **Method:**

  `GET`

* **URL Params**


* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:** 
    ``` javascript
      {
          "comment": {
             [comment1 data,
             comment2 data,
             comment3 data
             ] 
          }
      }
    ```

* **Error Response:**

  * **Code:** 403 Forbidden<br />
    **Content:** 
    ``` javascript
      {
          "detail": "Authentication Required"
      }
    ```


* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/comments/",
  type : "GET",
  success : function(r) {
    console.log(r);
  }
});
```


* **Notes:**

  success response contains all the comment's info, the `personal` boolean value shows whether the currently logged-in user is the original creator of the comment or not (the JWT token must be included in the `Authorization` header) and the `liked` boolean value shows if he liked it or not, if the user is not logged-in the value of `liked` will be `false`.


## **get single comment**
----
  get all the info of a single comment by providing it's `id`.

* **URL**

  `/api/comments/:id`

* **Method:**

  `GET`

* **URL Params**

| parameter      | required           | description                                         |
| :------------: | :----------------: | :-------------------------------------------------- |
| `id`[integer] | :heavy_check_mark: | the id of the comment that you would like to read |


* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:** 
    ``` javascript
      {
          "comment": {
              comment data
          }
      }
    ```

* **Error Response:**

  * **Code:** 404 Not found<br />
    **Content:** 
    ``` javascript
      {
          "msg": "comment not found"
      }
    ```


* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/comments/15",
  type : "GET",
  success : function(r) {
    console.log(r);
  }
});
```


* **Notes:**

  success response contains all the comment's info, the `personal` boolean value shows whether the currently logged-in user is the original creator of the comment or not (the JWT token must be included in the `Authorization` header) and the `liked` boolean value shows if he liked it or not, if the user is not logged-in the value of `liked` will be `false`.


## **delete comment**
----
  delete an existing personal comment by providing it's `comment_id`.

* **URL**

  `/api/comments/:id`

* **Method:**

  `DELETE`

* **Request Body Params**



* **Success Response:**

  * **Code:** 204 Not Content<br />
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
                  "msg": "comment id is missing or invalid",
                  "param": "comment_id"
              }
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
  url: "/api/comments/5",
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

  request must include the JWT token in the `Authorization` header, not including the token would result in an HTTP response code of 401 Unauthorized. a non-401 fail response contains an array of errors, trying to delete an comment that was created by someone else would result in an HTTP response code of 401 Unauthorized.