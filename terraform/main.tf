# Configure the AWS Provider
provider "aws" {
  region  = var.region
  profile = "samay-aws"
}

resource "aws_instance" "webserver" {
  ami                    = var.ami
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.sg.id]

  user_data = file("user-data.sh")

  tags = {
    Name = "web_instance"
  }
}