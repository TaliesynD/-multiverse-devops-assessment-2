provider "aws" {
region = "eu-west-2"
}
resource "aws_s3_bucket" "this" {
bucket_prefix = "mvws10-malc"
force_destroy = true
tags = {
Name = "Multiverse WS10 Bucket"
}
}
resource "aws_s3_object" "test_file" {
bucket = aws_s3_bucket.this.id
key = "test_file.txt"
content = "hello world!"
}
