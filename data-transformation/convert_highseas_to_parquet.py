import pandas as pd

def convert_highseas_csv_to_parquet(
    input_csv: str = "SAU-HighSeas-71-v48-0.csv",
    output_parquet: str = "SAU-HighSeas-71-v48-0.parquet"
) -> None:
    """
    Convert Sea Around Us High Seas CSV data to Apache Parquet format.

    This script reads the High Seas fisheries dataset (Pacific, Western Central),
    converts it from CSV to Parquet to optimize storage and query performance
    in Amazon Athena.

    Parameters
    ----------
    input_csv : str
        Path to the input CSV file
    output_parquet : str
        Path where the Parquet file will be written
    """

    # Load CSV into DataFrame
    df = pd.read_csv(input_csv)

    # Write Parquet file
    df.to_parquet(output_parquet, engine="pyarrow")

    print(f"✅ Converted {input_csv} → {output_parquet}")


if __name__ == "__main__":
    convert_highseas_csv_to_parquet()