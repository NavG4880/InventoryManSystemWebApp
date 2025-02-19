# AWS Scalable & Secure Web Application Deployment Project (CloudFormation)

## Overview
This project deploys a **highly available web application** using AWS CloudFormation.
Web App: A simple Flask-based app to manage parts inventory.
Database: Amazon RDS (PostgreSQL).
Deployment: AWS EC2, RDS, ALB, and CloudFormation.
CI/CD: GitHub Actions for automation.

## Architecture
- VPC with Public & Private Subnets
- Auto Scaling EC2 Instances with Load Balancer
- RDS Database (MySQL) in Private Subnet
- Security hardened using IAM, Security Groups, and WAF
- CI/CD using GitHub Actions & AWS CloudFormation

## How to Deploy
1. Clone the repository  
2. Run `aws cloudformation deploy`  
3. Access the web app via the Load Balancer URL  

Get help: [Post in our discussion board](https://github.com/orgs/skills/discussions/categories/introduction-to-github) &bull; [Review the GitHub status page](https://www.githubstatus.com/)

&copy; 2024 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

</footer>
