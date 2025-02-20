## Inventory Management System Deployment on AWS

### 📌 Project Overview  
This project demonstrates the deployment of an **Inventory Management System** web application using **AWS services**. The application runs on an **EC2 instance**, connects to an **RDS PostgreSQL database**, and is packaged as a **Docker container** managed via **AWS ECR**. The deployment is automated using **GitHub Actions** and **AWS CloudFormation**.

---

## 🚀 Architecture

The project follows this architecture:

1. **AWS EC2** – Hosts the web application inside a Docker container.  
2. **AWS RDS (PostgreSQL)** – Stores inventory management data.  
3. **AWS CloudFormation** – Automates infrastructure provisioning.  
4. **AWS ECR** – Manages Docker container images.  
5. **GitHub Actions** – Automates deployment using CI/CD pipeline.  
6. **AWS Systems Manager (SSM)** – Stores and retrieves database credentials securely.  
7. **AWS IAM Roles** – Grants necessary permissions for deployments.  

---

## 📂 Project Structure  

```
├── deployment/
│   ├── cloudformation.yaml   # AWS CloudFormation template for infrastructure
│   ├── Dockerfile            # Dockerfile to containerize the application
│   ├── deploy.yml            # GitHub Actions workflow for CI/CD
├── app/                      # Web application source code (Flask-based)
│   ├── app.py               # Entry point for the Flask app
│   ├── requirements.txt      # Python dependencies
│   ├── templates/            # HTML templates- place all html pages here
│   ├── static/               # CSS, JS, and images
├── README.md                 # Project documentation
```

---

## 🛠️ Prerequisites  

- **AWS Account** with access to EC2, RDS, IAM, and ECR  
- **GitHub Repository** to store project files  
- **Docker** installed locally  
- **AWS CLI** and **AWS IAM permissions** configured  
- **GitHub Secrets** configured for AWS access  

---

## 🔧 Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/inventory-management-system.git
cd inventory-management-system
```

### 2️⃣ Configure AWS Secrets in GitHub  
Go to **GitHub → Your Repository → Settings → Secrets and Variables → Actions** and add:  
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_PASSWORD`

### 3️⃣ Build and Push Docker Image  

```bash
docker build -t inventory-management-app .
docker tag inventory-management-app <AWS_ECR_URI>/inventory-management-app:latest
docker push <AWS_ECR_URI>/inventory-management-app:latest
```

### 4️⃣ Deploy Infrastructure using CloudFormation  

Run the following command to deploy your CloudFormation stack:

```bash
aws cloudformation create-stack --stack-name InventoryAppStack \
    --template-body file://deployment/cloudformation.yaml \
    --capabilities CAPABILITY_NAMED_IAM
```

Wait for the stack to be deployed. You can check the status on the **AWS CloudFormation Console**.

---

## ⚙️ GitHub Actions CI/CD Pipeline  

The **GitHub Actions Workflow (`deploy.yml`)** automates the build and deployment:

- **Step 1:** Checks out the repository  
- **Step 2:** Logs into **Docker Hub**  
- **Step 3:** Builds and pushes the Docker image to **AWS ECR**  
- **Step 4:** Configures **AWS credentials**  
- **Step 5:** Deploys the CloudFormation stack  

### 🔄 Enable GitHub Actions Deployment  
By default, the workflow is disabled (`on: none`). To enable it, update `deploy.yml`:

```yaml
on:
  push:
    branches:
      - main
```

Commit and push the changes to trigger the workflow.

---

## 📊 Monitoring and Logs  

1. **EC2 Logs**  
   - SSH into the instance:  
     ```bash
     ssh -i your-key.pem ec2-user@<EC2_PUBLIC_IP>
     ```
   - View logs:  
     ```bash
     cat /var/log/user-data.log
     ```

2. **Docker Logs**  
   ```bash
   docker logs <CONTAINER_ID>
   ```

3. **CloudFormation Events**  
   ```bash
   aws cloudformation describe-stack-events --stack-name InventoryAppStack
   ```

---

## 🛑 Cleaning Up  

To **delete all resources** and avoid unwanted costs:  

1. Delete the CloudFormation stack:  
   ```bash
   aws cloudformation delete-stack --stack-name InventoryAppStack
   ```

2. Deregister the Docker image from ECR:  
   ```bash
   aws ecr batch-delete-image --repository-name inventory-management-app --image-ids imageTag=latest
   ```

3. Delete the RDS database manually from the **AWS RDS Console**.

---

## 🎯 Future Enhancements  

- ✅ Implement **AWS ALB** for better load balancing  
- ✅ Use **Terraform** instead of CloudFormation for better flexibility  
- ✅ Enable **AWS Lambda** for auto-scaling  
- ✅ Add **Unit Tests** and automated security checks  
