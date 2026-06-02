# Step 1: Specify the required provider (Kubernetes)
terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.10"
    }
  }
}

# Step 2: Configure the Kubernetes Provider to connect to local Docker Desktop cluster
provider "kubernetes" {
  config_path = "~/.kube/config"
}

# Step 3: Create a dedicated Namespace for our Fraud Detection System
resource "kubernetes_namespace" "fraud_namespace" {
  metadata {
    name = "fraud-detection-system"
  }
}