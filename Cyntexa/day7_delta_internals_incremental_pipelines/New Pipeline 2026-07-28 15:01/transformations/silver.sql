create streaming table dev.silver.sales_cleaned_st as 
select distinct * except(`_rescued_data`, `file_path`, ingestion_date) from stream (dev.bronze.sales_st) where order_id is not null;



create materialized view dev.gold.total_amount_mv as 
select round(sum(total_amount)) as total_amount from dev.silver.sales_cleaned_st;


