# AudiofilesDjangoAPI
Django API for CREATE, GET, UPDATE and DELETE operations.

URLS cheatsheet:
======

* **GET**
  * Display all of a single filetype : 'audioapp/<str:filetype>/' (eg: 'audioapp/song/')
  * Display a particular record : 'audioapp/<str:filetype>/<int:fileid>/' (eg : 'audioapp/song/1')
* **CREATE**
  * Create a new record of a particular filetype : 'audioapp/<str:filetype>/create' (eg:'audioapp/song/create')
* **UPDATE**
  * Update an existing record of a filetype : 'audioapp/<str:filetype>/<int:fileid>/update' (eg:'audioapp/song/1/update')
* **DELETE**
  * Delete an exisitng record of a filetype : 'audioapp/<str:filetype>/<int:fileid>/delete' (eg:'audioapp/song/1/delete')

How to view database:
======

* **Superuser details**
  * usernanem - admin
  * password - password
* Login in at '/admin'
* Enjoy

