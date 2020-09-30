# cvs

Guests can read cvs, signed-in users can read, create, update or delete cvs.

## **create cv**
----
  create a new cv and set it's `file` and `user` to the given arguments, a sucess response contains the id of the created cv.

* **URL**

  `/api/cvs`

* **Method:**

  `POST`

* **Request Body Params**

| parameter          | required           | description                                                                                                                                                                                         |
| :----------------: | :----------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file`[file]       | :heavy_check_mark: | desired file                                                                                                        |
| `user`[intger]     | :heavy_check_mark: | user who upload who's cv                                                                                                           |

* **Success Response:**

  * **Code:** 201 Created<br />
    **Content:** 
    ``` javascript
      {
        "msg": "successful",
        "id": "javascript-tutorial-HJ_avCy2M" 
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
  url: "/api/cvs",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : {
	"file": "choose file",
	"user" :5
	
},
  type : "POST",
  success : function(r) {
    console.log(r);
  }
});
```

* **Notes:**

  request must include the JWT token in the `Authorization` header, not including the token would result in an HTTP response code of 401 Unauthorized, a success response will always contain the id of the cv, you can request the cv using this id, check the <a href="#/cvs?id=get-single-cv" class="anchor">"get single cv"</a> section for an example.


## **update cv**
----
  update an existing personal cv's `file`.

* **URL**

  `/api/cvs/:id`

* **Method:**

  `PATCH`

* **Request Body Params**

| parameter              | required           | description                                                                                                                                                                                             |
| :--------------------: | :----------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `file`[file]           | :heavy_check_mark: | the new personal cv that you would like to update                                                                                                                                            |

* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:** 
    ``` javascript
      {
          "msg": "successful",
          "cv": {
              "file": "file"
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
                  "msg": "cv id is missing or invalid",
                  "param": "cv_id"
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
  url: "/api/cvs/5",
  headers: {
        'Content-Type':'application/json',
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjk0LCJpYXQiOjE1MjE2NDY1NTQsImV4cCI6MTUyMTY1NzM1NH0.egYak11OPvigG0Fd67u3d2GKc6YcIH1wUd2hZIm6Vm4'
    },
  dataType: "json",
  data : {
	"file": "choose file",
},
  type : "PATCH",
  success : function(r) {
    console.log(r);
  }
});
```


* **Notes:**

  a request must only include the fields that the user wants to update and must include the JWT token in the `Authorization` header, not including the token would result in an HTTP response code of 401 Unauthorized. a non-401 fail response contains an array of errors, if it doesn't that means no fields were sent in the request body, trying to update an cv that was created by someone else would result in an HTTP response code of 401 Unauthorized, success response contains the updated fields.

## **get all cvs**
----
  get all the info of a all cvs.

* **URL**

  `/api/cvs/`

* **Method:**

  `GET`

* **URL Params**


* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:** 
    ``` javascript
      {
          "cv": {
             [cv1 data,
             cv2 data,
             cv3 data
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
  url: "/api/cvs",
  type : "GET",
  success : function(r) {
    console.log(r);
  }
});
```


* **Notes:**

  success response contains all the cv's info, the `personal` boolean value shows whether the currently logged-in user is the original creator of the cv or not (the JWT token must be included in the `Authorization` header) and the `liked` boolean value shows if he liked it or not, if the user is not logged-in the value of `liked` will be `false`.


## **get single cv**
----
  get all the info of a single cv by providing it's `id`.

* **URL**

  `/api/cvs/:id`

* **Method:**

  `GET`

* **URL Params**

| parameter      | required           | description                                         |
| :------------: | :----------------: | :-------------------------------------------------- |
| `id`[integer] | :heavy_check_mark: | the id of the cv that you would like to read |


* **Success Response:**

  * **Code:** 200 OK<br />
    **Content:** 
    ``` javascript
      {
          "cv": {
              cv data
          }
      }
    ```

* **Error Response:**

  * **Code:** 404 Not found<br />
    **Content:** 
    ``` javascript
      {
          "msg": "cv not found"
      }
    ```


* **Sample Call:**

``` javascript
$.ajax({
  url: "/api/cvs/15",
  type : "GET",
  success : function(r) {
    console.log(r);
  }
});
```


* **Notes:**

  success response contains all the cv's info, the `personal` boolean value shows whether the currently logged-in user is the original creator of the cv or not (the JWT token must be included in the `Authorization` header) and the `liked` boolean value shows if he liked it or not, if the user is not logged-in the value of `liked` will be `false`.


## **delete cv**
----
  delete an existing personal cv by providing it's `cv_id`.

* **URL**

  `/api/cvs/:id`

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
                  "msg": "cv id is missing or invalid",
                  "param": "cv_id"
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
  url: "/api/cvs/5",
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

  request must include the JWT token in the `Authorization` header, not including the token would result in an HTTP response code of 401 Unauthorized. a non-401 fail response contains an array of errors, trying to delete an cv that was created by someone else would result in an HTTP response code of 401 Unauthorized.