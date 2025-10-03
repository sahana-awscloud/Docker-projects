This guide explains how to install AWS CLI, configure it, log in to ECR, create a Docker image, and push it to ECR.

1. Install AWS CLI (Refer : https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. Verify AWS CLI Installation
       aws --version
3. Configure AWS CLI
       aws configure
   You will be asked for:
    AWS Access Key ID
    AWS Secret Access Key
    Default region name (example: us-east-1)
    Default output format (json, table, or text)
4. Create ECR Repository
       aws ecr create-repository --repository-name <your_repo_name> --region <your_region>
5. Install Docker Desktop (Refer : https://www.docker.com/products/docker-desktop)
   Post installation, verify if Docker is installed - docker --version
6. Authenticate Docker with ECR
       aws ecr get-login-password --region <your_region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<your_region>.amazonaws.com
7. Create Dockerfile
8. Build Docker Image
       docker build -t first-docker-python-app .
9. Tag Docker Image for ECR
        docker tag first-docker-python-app:latest <account_id>.dkr.ecr.us-east-1.amazonaws.com/<your-repo>:latest
10. Push Docker Image to ECR
        docker push <account_id>.dkr.ecr.us-east-1.amazonaws.com/my-docker-app:latest
    <img width="1531" height="412" alt="image" src="https://github.com/user-attachments/assets/d6d775ea-5f37-49e0-82f7-76512d5cba6e" />
12. Verify Image in ECR
        aws ecr list-images --repository-name my-docker-app --region us-east-1 --output table
    <img width="1115" height="253" alt="image" src="https://github.com/user-attachments/assets/530d71fd-5cd1-476a-a35c-987cfa116925" />


Summary
Installed & configured AWS CLI

Created an ECR repo

Installed Docker

Built → Tagged → Pushed a Docker image

Verified image inside AWS ECR
