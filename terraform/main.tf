terraform {
  required_version = ">= 1.5.0"
}

resource "local_file" "devops_health_api" {
  filename = "${path.module}/devops-health-api.txt"

  content = <<-EOT
    DevOps Health API infrastructure managed by Terraform.
    Application: devops-health-api
    Container Port: 8000
  EOT
}
