variable "aws_region" {
  default = "ap-south-1"
}

variable "vpc_cidr" {
  type        = string
  description = "This is vpc_cidr"
  default     = "10.0.0.0/16"
}

variable "subnet_cidr_public" {
  type        = string
  description = "This is publci subnet cidr"
  default     = "10.0.0.0/17"
}

variable "subnet_cidr_private" {
  type        = string
  description = "this is public subnet cidr"
  default     = "10.0.128.0/17"
}

variable "availability_zone_public" {
  type        = string
  description = "Which zone subnet is residing"
  default     = "ap-south-1a"
}

variable "availability_zone_private" {
  type        = string
  description = "which zone subnet is residing"
  default     = "ap-south-1a"
}

variable "instance_type" {
  type        = string
  default     = "t2.micro"
  description = "Ec2 instance type"
}

variable "key_name" {
  description = "Ec2 instance key pair name"
}

variable "ami_id" {
  description = "Ec2 instance ami id"
}



