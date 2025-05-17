## 🛠 Setup Steps

## 1. Clone the Repo

```
git clone https://github.com/RubenCroes/PE-assignment-3.git
```

### 2. Build and Push Docker Image

```
# Create ECR
aws ecr create-repository --repository-name flask-app

# Authenticate with ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.us-east-1.amazonaws.com

# Build and tag
docker build -t flask-crud-app .
docker tag flask-crud-app:latest <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/flask-crud-app:latest

# Push to ECR
docker push <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/flask-crud-app:latest

```

### 3. Deploy Infrastructure with Terraform

```
terraform init
terraform apply
```
