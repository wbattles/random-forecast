import get_weather as rpt
import boto3

def lambda_handler(event, context):

    s3 = boto3.client("s3")

    file_path = "/tmp/cordinates.csv"
    bucket = "random-forecast-data"
    key = "cordinates.csv"

    s3.download_file(bucket, key, file_path)

    cordinates = rpt.getCords()
    endpoint = rpt.getEndpoint(cordinates)
    city = rpt.cityData(cordinates)
    forecast = rpt.getForecast(endpoint, city)
    
    return forecast