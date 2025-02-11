import requests
from datetime import datetime, timedelta


# def a function to download taxi trip record data from the cloudfront
def download_taxi_data(
    start_year, start_month, end_year, end_month, taxi_type="yellow"
):
    current_date = datetime(start_year, start_month, 1)
    end_date = datetime(end_year, end_month, 1)

    while current_date <= end_date:
        year = current_date.year
        month = f"{current_date.month:02d}"
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year}-{month}.parquet"
        filename = f"./input/data/{taxi_type}_tripdata_{year}-{month}.parquet"

        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed: {filename} (HTTP {response.status_code})")

        # Move to next month
        current_date = current_date + timedelta(days=32)
        current_date = current_date.replace(day=1)


if __name__ == "__main__":

    download_taxi_data(2024, 1, 2024, 2, "yellow")
    download_taxi_data(2024, 1, 2024, 2, "green")
