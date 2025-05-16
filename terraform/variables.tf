variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "rds_username" {
  description = "RDS master username"
  type        = string
}

variable "rds_password" {
  description = "RDS master password"
  type        = string
  sensitive   = true
}

variable "rds_db_name" {
  description = "RDS database name"
  default     = "flaskdb"
}

variable "ecr_image_url" {
  default = "339712812036.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest"
}