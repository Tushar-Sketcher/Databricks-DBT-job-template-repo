from dbt.logger import GLOBAL_LOGGER as logger
def model(dbt, spark):
    df = spark.sql('select *from example.test')
    return df
