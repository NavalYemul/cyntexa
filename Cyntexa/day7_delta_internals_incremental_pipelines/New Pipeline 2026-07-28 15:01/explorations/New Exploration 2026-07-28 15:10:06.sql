-- Databricks notebook source
select * from read_files("/Volumes/dev/demo/raw/sales/")

-- COMMAND ----------

select distinct * from dev.bronze.sales_st where order_id is not null

-- COMMAND ----------

select round(sum(total_amount)) as total_amount from dev.silver.sales_cleaned_st

-- COMMAND ----------

view: 
1 query 10 sec
2 query 10 sec
3 query 10 sec
1000 query 10 sec 


Materilaised view

1 query 10 sec ( store the result in cache)
2 query 2 sec 