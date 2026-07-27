from pyspark.sql import DataFrame
from pyspark.sql.functions import col, when



def convert_yes_no_to_boolean(
    df: DataFrame,
    column_name: str
) -> DataFrame:
    """
    Convert a Yes/No column into a Boolean column

    Parameters
    -----------
    df : DataFrame
        Input Spark DataFrame.

    column_name : str
        Name of the column to convert.

    Returns
    --------
    DataFrame
        DataFrame with specified column converted to Boolean values.
    """


    return df.withColumn(
        column_name,
        when(col(column_name) == "Yes", True)
        .when(col(column_name) == "No", False)
        .otherwise(None)
    )


nuga_df = convert_yes_no_to_boolean(
    nuga_df,
    "Is_Active"
)