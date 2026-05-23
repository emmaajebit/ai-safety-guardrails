# S3 Backend with State Locking for Terraform

terraform {
  backend "s3" {
    bucket         = "ai-safety-terraform-state"
    key            = "guardrails/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "ai-safety-state-lock"  # For locking
    encrypt        = true
  }
}

# DynamoDB table for state locking
resource "aws_dynamodb_table" "terraform_state_lock" {
  name         = "ai-safety-state-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
