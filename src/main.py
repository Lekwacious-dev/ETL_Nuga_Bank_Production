# from extract import extract_data
# from transform import clean_transactions
# from transform import normalize_data
# from load import load_to_postgres


# def main() -> None:
#     """
#     Execute the complete ETL pipeline.
#     """
#     spark = create_spark_session()

#     transactions_df = extract_data(spark)

#     cleaned_df = clean_transactions(transactions_df)

#     normalized_data = normalize_data(cleaned_df)

#     load_to_postgres(normalized_data)


# if __name__ == "__main__":
#     main()