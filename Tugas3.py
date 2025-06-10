import pandas as pd

stunting_data = pd.read_csv("F:/Arif Files/Semester 8/PraktikumPembelajaranMesin-SMT8/TUGAS 3/vertikalkementerian-2-od_20735_prevalensi_balita_stunting__kabupatenkota_v3_data.csv")
air_quality_data = pd.read_csv("F:/Arif Files/Semester 8/PraktikumPembelajaranMesin-SMT8/TUGAS 3/Air_Quality.csv")

def classify_data_type(column, series):
    if pd.api.types.is_numeric_dtype(series):
        if (series == 0).any():
            return "Rasio"
        else:
            return "Interval"
    elif series.dtype == object:
        if "tahun" in column.lower() or "time period" in column.lower():
            return "Ordinal"
        else:
            return "Nominal"
    return "Nominal"

stunting_data_types = {col: classify_data_type(col, stunting_data[col]) for col in stunting_data.columns}
stunting_data_types_df = pd.DataFrame(list(stunting_data_types.items()), columns=["Kolom", "Jenis Data"])
print("Jenis Data untuk Dataset Stunting:")
print(stunting_data_types_df)

# Klasifikasi untuk dataset air quality
air_quality_data_types = {col: classify_data_type(col, air_quality_data[col]) for col in air_quality_data.columns}
air_quality_data_types_df = pd.DataFrame(list(air_quality_data_types.items()), columns=["Kolom", "Jenis Data"])
print("\nJenis Data untuk Dataset Air Quality:")
print(air_quality_data_types_df)
