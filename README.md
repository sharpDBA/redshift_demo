##  Demo: Create table in AWS Redshift with 3 columns

Project directory tree.  

```
redshift_demo
|	README.md
|	conn.py
|	cred.py
|	run_query.py
```

###Requirements: 

* AWS Redshift cluster
* PostgreSQL (local installation)
* Python
	* psycopg2 

### File contents

The **conn.py** file should contain the variables for:  

* AWS Redshift cluster host / endpoint

The **cred.py** file should contain the variables for:  

* AWS Redshift cluster database user.  
* AWS Redshift cluster database password.

The **run_query.py** file contains and executes the query to create a table called "test."

---
Note that for this template, the connection related variables are generated through user input. 

---

### Future version plans: 
Feature additions:   
+-- Store SQL scripts and queries outside of the run_query.py file.   
+-- Add a way for the user to specify which SQL to run when running the execution script. 