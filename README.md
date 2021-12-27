# Databases
DB project using PostgreSQL and Python

This project connects between Python application and PostgreSQL database using psycopg2 library.
The user can choose between several queries in the menu.

The Program shows a menu of 5 options:
1. returns the number of distinct cities whose name starts with 'L' where a match was played.
2. returns the distinct countries that hosted the FIFA World Cup and how many times they hosted the tournament. Order by count descending, then alphabetically.
3. List the various types of tournaments played by Greece. List alphabetically.
4. Select the country with the most wins in shootouts(the country name and the number of wins).
5. exit the program

For running the program:
1. Create a database in PostgreSQL named footballdb.
2. run the dbm_create_tables.sql
3. run the main python file: dbm.py
