# Databricks notebook source
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, TimestampType

# Define schema
yellow_taxi_schema = StructType([
    StructField("VendorID", IntegerType(), True),                  # Vendor code
    StructField("tpep_pickup_datetime", TimestampType(), True),    # Pickup timestamp
    StructField("tpep_dropoff_datetime", TimestampType(), True),   # Dropoff timestamp
    StructField("Passenger_count", IntegerType(), True),           # Number of passengers
    StructField("Trip_distance", DoubleType(), True),              # Distance in miles
    StructField("Pickup_longitude", DoubleType(), True),           # Pickup longitude
    StructField("Pickup_latitude", DoubleType(), True),            # Pickup latitude
    StructField("RateCodeID", IntegerType(), True),                # Rate code
    StructField("Store_and_fwd_flag", StringType(), True),         # Y/N
    StructField("Dropoff_longitude", DoubleType(), True),          # Dropoff longitude
    StructField("Dropoff_latitude", DoubleType(), True),           # Dropoff latitude
    StructField("Payment_type", IntegerType(), True),              # Payment type code
    StructField("Fare_amount", DoubleType(), True),                # Meter fare
    StructField("Extra", DoubleType(), True),                      # Extra charges
    StructField("MTA_tax", DoubleType(), True),                    # MTA tax
    StructField("Improvement_surcharge", DoubleType(), True),      # Improvement surcharge
    StructField("Tip_amount", DoubleType(), True),                 # Tip
    StructField("Tolls_amount", DoubleType(), True),               # Tolls
    StructField("Total_amount", DoubleType(), True)                # Total fare charged
])


# COMMAND ----------

import dlt

# COMMAND ----------

@dlt.table(
    name="nyc_taxi.default.bronze_data",
    comment="Bronze Table",
    table_properties={"quality": "bronze"}
)
def bronze_table():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .schema(yellow_taxi_schema)
        .load("/Volumes/nyc_taxi/nyc_taxi/data/")
    )


# COMMAND ----------

@dlt.table(
    name="nyc_taxi.default.silver_data",
    comment="Silver Table without null ids",
    table_properties={"quality": "silver"}
)
def silver_table():
    return (
        spark.readStream.table("nyc_taxi.default.bronze_data")
        .select("*")
        .where(
            "VendorID IS NOT NULL AND tpep_pickup_datetime IS NOT NULL AND tpep_dropoff_datetime IS NOT NULL AND (RateCodeID IS NULL OR RateCodeID in (1,2,3,4,5,6)) AND (payment_type IS NULL OR payment_type in (1,2,3,4,5,6))"
        )
    )


# COMMAND ----------

# Materialized View
import dlt
from pyspark.sql import functions as F

@dlt.table(
    name="nyc_taxi.default.daily_revenue",
    comment="Materialized view for daily revenue analytics",
    table_properties={"quality": "gold"}
)
def daily_revenue():
    return (
        dlt.read("nyc_taxi.default.silver_data")
        .groupBy("VendorID", F.to_date("tpep_pickup_datetime").alias("pickup_date"))
        .agg(
            F.sum("total_amount").alias("total_revenue"),
            F.avg("trip_distance").alias("avg_trip_distance"),
            F.count("*").alias("trip_count"),
            F.sum("tip_amount").alias("total_tip_amount")      # New aggregation
        )
    )
