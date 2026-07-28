create streaming table dev.bronze.sales_st as
 select *,current_timestamp() as ingestion_date, _metadata.file_path as file_path from stream read_files("/Volumes/dev/demo/raw/sales/")