# Project: NoSQL

*   0-list_databases
    - Write a script that lists all databases in MongoDB.

*   1-use_or_create_database
    - Write a script that creates or uses the database `my_db`

*   2-insert
    - Write a script that inserts a document in the collection `school`:
      - The document must have one attribute `name` with value “Holberton school”
      - The database name will be passed as option of `mongo` command

*   3-all
    - Write a script that lists all documents in the collection `school`:
      - The database name will be passed as option of `mongo` command

*   4-match
    - Write a script that lists all documents with `name="Holberton school"` in the collection `school`:
      - The database name will be passed as option of `mongo` command

*   5-count
    - Write a script that displays the number of documents in the collection `school`:
      - The database name will be passed as option of `mongo` command

*   6-update
    - Write a script that adds a new attribute to a document in the collection `school`:
      - The script should update only document with `name="Holberton school"` (all of them)
      - The update should add the attribute `address` with the value “972 Mission street”
      - The database name will be passed as option of `mongo` command

*   7-delete
    - Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:
      - The database name will be passed as option of `mongo` command
