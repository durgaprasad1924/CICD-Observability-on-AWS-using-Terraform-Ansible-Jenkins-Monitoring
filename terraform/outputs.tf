output "jenkins_public_ip" {
  value = aws_instance.jenkins.public_ip
}

output "ssh_command" {
  value = "ssh -i ${var.key_name}.pem ec2-user@${aws_instance.jenkins.public_ip}"
}

