##  Demo: Create table in AWS Redshift with 3 columns

### Simplified Instructions:  
1) Clone the redshift_demo directory.
2) Run run_query.py and follow the prompts.

#### What you need: 
* AWS Redshift cluster
* PostgreSQL (local installation)
* Python 3.x
	* psycopg2 

#### Requirements: 
Project directory tree.  

```
redshift_demo
|	README.md
|	conn.py
|	cred.py
|	run_query.py
```

#### File contents

The **conn.py** file should contain or generate the variables for:  

* AWS Redshift cluster host / endpoint

The **cred.py** file should contain or generate the variables for:  

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
