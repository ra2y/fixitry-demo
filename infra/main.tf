# INTENTIONALLY INSECURE AND NON-DEPLOYABLE DEMO INFRASTRUCTURE.
# Do not run terraform apply. Trivy should inspect this file statically.

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

resource "aws_security_group" "securefix_demo" {
  name        = "securefix-intentionally-insecure-demo"
  description = "Never deploy: permits public SSH for a Trivy demonstration"

  ingress {
    description = "INTENTIONALLY INSECURE public SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "securefix_demo" {
  bucket = "securefix-intentionally-insecure-demo-never-deploy"
}

resource "aws_s3_bucket_public_access_block" "securefix_demo" {
  bucket = aws_s3_bucket.securefix_demo.id

  # INTENTIONALLY INSECURE: all public-access protections are disabled.
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

