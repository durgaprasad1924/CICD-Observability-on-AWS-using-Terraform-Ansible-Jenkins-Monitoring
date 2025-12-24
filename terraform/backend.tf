terraform {
  backend "s3" {
    bucket         = "my-bucket-dp1"
    key            = "my-bucket-dp1/folder"
    encrypt        = true
    dynamodb_table = "terraform-tr"
    region         = "ap-south-1"
  }
}
