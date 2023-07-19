
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "this" {
  bucket = "random-forecast-data"
}

resource "aws_s3_object" "cordinates_file" {
  key = "cordinates.csv"
  source = "./cordinates.csv"
  bucket = aws_s3_bucket.this.bucket
}


data "archive_file" "zip_the_python_code" {
  type        = "zip"
  source_dir  = "./lambda"
  output_path = "./lambda.zip"
}

resource "aws_lambda_function" "this"{

  function_name     = var.function_name
  layers            = var.layers
  role              = var.lambda_role

  handler           = "index.lambda_handler"
  runtime           = "python3.10"
  filename          = "./lambda.zip"

}

resource "aws_s3_bucket_notification" "aws-lambda-trigger" {
  bucket = "${aws_s3_bucket.this.id}"

  lambda_function {
    lambda_function_arn = "${aws_lambda_function.this.arn}"
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "file-prefix"
    filter_suffix       = "file-extension"
  }

}

resource "aws_lambda_permission" "test" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.this.function_name}"
  principal     = "s3.amazonaws.com"
  source_arn    = "arn:aws:s3:::${aws_s3_bucket.this.id}"
}