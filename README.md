# Databricks-DBT-job-template-repo
### Data Engineering DBT-Databricks Template Repo
This repository provides a sample template for a DBT-Databricks project. Inside, you'll find the folder structure and a step-by-step guide on how to generate the Databricks-DBT project using the template repo outlined.

The repository represents the below tree structure for the folders/files added in. This structure organizes DBT models, macros and tests into a separate directory called dbt for clarity. 


### Significance of profiles.yml in above template
The above template does not include profiles.yml which is used to provide connection details of the DBT jobs being executed. Once you generate the project repo from template and deploy the workflow on databricks, the sample dbt jobs added in above template will run on the sql warehouse (using warehouse_id) with its relevant databricks host (lab/stage/prod).
The reason we haven’t included profiles.yml is, when you run the DBT job’s on sql warehouse( using warehouse_id ) the sql warehouse inherently retrieves the connection details for the relevant host (lab/stage/prod), rendering the need for profiles.yml redundant ( The warhouse_id is specified in datbricks.yml file in above template )
Also the profiles.yml in a project directory increases the risk of committing credentials into version control. To lower the risk, we can use the DBT env_var jinja function(https://docs.getdbt.com/reference/dbt-jinja-functions/env_var) that helps to ingest environment variables into profiles.yml instead of hard coded credentials, which we can explore in the future if needed. This might need some extra work setting up the environmental variables.
However if you intend to utilize an All-purpose cluster for running DBT jobs, including profiles.yml becomes essential. An all purpose cluster is a cluster type that can handle a variety of workloads, including DBT jobs. When running DBT jobs on all purpose cluster the profiles.yml serves as a means of connection to your database or data warehouses. This file typically contains details such as the database hostname, port, username, password, and other connection parameters (Databricks Doc).
