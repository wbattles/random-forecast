variable "bucket" {
  description = "S3 bucket name"
  type        = string
}

variable "function_name"{
    description = "Lambda function name"
    type        = string
}

variable "layers" {
  type        = list(string)
  description = "Lambda layer (ARN)"
}

variable lambda_role {
    type        = string
    description = "IAM role for lambda function (ARN)"
}