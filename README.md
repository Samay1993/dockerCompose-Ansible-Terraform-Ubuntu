## Task description:

There are basically 3 different set of tasks that have been completed:
1. Running a python application along postgres using Ansible.
2. Created terraform configurations to deploy the whole stack on EC2 Instance
3. Explain how monitoring could be acheived if there were multiple EC2 instances running Ubuntu Sever with our application in it.


## Tech Stack Used:
* Python (Flask)
* Postgres
* Docker and Docker-Compose
* Ansible
* Terraform
* AWS EC2 Instance

## Pre-Requisites:
There are few pre-requisites to start with this project as follows:
* Python and PIP
* Docker Setup
* Ansible
* AWS Account and CLI configurations
* Terraform 

## Application Details:
Basically our applications is built using Python and Flask which connects with Postgres database, and insert some data into the table and then retrieves it using two seperate endpoints as below:
- /insert - Insert values in the database table
- /fetch - Fetch values from database.

>Note: If you run the application locally, it will run on "127.0.0.1:5000" attach endpoints as required.

## Task 1:
Task involves below steps:
- Dockerizing the application and running it with another postgres database instance and test it functionalities, which can be achieved by running following commands:
    + docker build -t _image-tag_ .
    + docker network create --subnet 172.168.1.0/24 _network-name_
    + docker run -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=mydatabase -d --name postgres -p 5432:5432 --network _network-name_ postgres:13 
    + docker run --name _container-name_ -p 4000:5000 --network _network-name_ _image-tag_
    > Note: We are creating a network, so both out containers run in the same network and can be connected together, in addition to that we are providing database details as environment variable along with postgres.<br>
    > We are also mapping our python container with _4000_ port on our host, so that application will be available at _  localhost:4000_

- Setting up our application in docker-compose, for that _docker-compose.yaml_ can be used like below:
    + docker-compose up --build
    > Note: The app will be available on _localhost:5555_

- Setting up Ansible configurations:
    + Ansible configurations are present in */ansible* directory
    + To start the application using Ansible run following command: _ansible-playbook ansible/playbook.yaml -i ansible/hosts_
    + To take down the application run following command: _ansible-playbook ansible/undeploy-playbook.yaml -i ansible/hosts_

## Task 2:
Task involves below steps:
- Setting up terraform configuration to setup ubuntu in an EC2 instace and running our application there, and this project acheives that like below:
    + Terraform configuration is done in _/terraform_ directory.
    + _user-data.sh_ is being used to pass certains commands that EC2 instance needs to run as soon as it starts which involves:
        - Installing dependencies
        - Cloning our repo
        - Starting the ansible setup
    + To deploy with terraform, make sure you have your terraform setup ready to deploy(make sure you update the profile name in provided block) and run below commands, once you are inside _/terraform_:
        - terraform fmt
        - terraform validate
        - terraform plan
        - terraform apply or terraform apply --auto-approve
    + In order to take down your project from AWS, just simply run _terraform destroy_ or _terraform destroy --auto-approve_.

-  To answer the question *How would you structure your Terraform project if you have multiple environments and use different cloud providers?*
    + There are different approach we can follow and honestly there's no right or wrong way to it, it completely depends on organizational's needs, but as per my understanding and experience we can follow below best practices:
        - Separate Terraform projects: Make a different Terraform project for every configuration of cloud service and environment. You could, for instance, have projects for production on AWS, staging on AWS, production on GCP, and so forth.
        - Utilize modules: To specify shared resources across environments and cloud providers, use Terraform modules. This will guarantee consistency while minimizing duplication.
        - To specify environment-specific configurations, such as VPC CIDR blocks, instance types, and so forth, use variables.
        - Utilize workspaces: To manage numerous environments inside of a single Terraform project, use Terraform workspaces. With distinct sets of state and variables for each environment, you can maintain the same Terraform codebase.
        - Use version control: To handle your Terraform codebase, use a version control system like Git. This enables you to keep note of changes and roll them back if required.
        - Use a naming convention: To make it simple to recognize your resources across environments and cloud providers, use a consistent naming strategy.
        - Use remote state storage: To store your Terraform state, use a remote state storage option like AWS S3 or HashiCorp Terraform Cloud. This will lessen the chance of data loss and guarantee consistency across environments.

## Task 3:
*Let's consider a scenario where we have multiple Ubuntu prod instances, then how should we monitor them? What should be our monitoring strategy?*

When we talk about monitoring there are few things to consider as follows:
* _Which moniroting tools meet our requirements_: Prometheus, Grafana, Nagios, Zabbix, and Datadog are examples of popular choices.
* _What do we want to monitor_: Means choose the data you want to track. CPU utilization, memory usage, disk usage, network traffic are a few important metrics to take into account.
* _How do we want to be notified when there's an issue_: Different monitoring tool offers different alert managers.
* _Dashboarding_: It's crucial to have a single dashboard from which you can view all of your metrics. An application like Grafana can be used for this.
* _Log monitoring_: Analyzing logs is also really important in identifying problems. ELK Stack, Loki can be used for this.
* _What happens if our monitoring system itself breaks_: Making in scalable is also as important as making our application scalable.

It is possible to monitor numerous Ubuntu prod EC2 instances using a variety of tools and techniques. Here are a few potential choices:
* _WatchCloud_: Amazon AWS resources and the apps you run on them are monitored by CloudWatch. Metrics, log files, and alerts can all be collected, tracked, and monitored using CloudWatch. A unified picture of metrics, logs, and events from various resources, including EC2 instances, is provided by it. You can keep an eye on your EC2 instances' CPU consumption, network traffic, disk usage, and other metrics with CloudWatch.
* _Prometheus_: Prometheus is an open-source monitoring system that collects metrics from configured targets, stores them, and can generate alerts based on defined rules. It has a powerful query language for analyzing collected data and creating dashboards. You can use Prometheus to monitor various metrics of your EC2 instances, such as CPU usage, memory usage, disk usage, and network traffic.
* _ELK Stack_: ELK Stack is a combination of three open-source tools: Elasticsearch, Logstash, and Kibana. Elasticsearch is a search and analytics engine, Logstash is a log collection and processing pipeline, and Kibana is a visualization tool. You can use ELK Stack to collect and analyze logs from your EC2 instances and their services, such as web servers, application servers, and databases.
* _Datadog_: Datadog is a cloud monitoring platform that provides monitoring and analytics for cloud-scale environments. It can monitor metrics, traces, and logs from various sources, including EC2 instances. Datadog can monitor your EC2 instances' CPU usage, memory usage, disk usage, and network traffic, as well as the performance of your applications and services running on them.

Overall, the monitoring strategy for multiple Ubuntu prod EC2 instances should involve collecting metrics, logs, and events from various sources and tools and storing them in a centralized location. This can help you identify performance issues, troubleshoot problems, and optimize resource utilization. Additionally, setting up alerts and notifications can help you respond quickly to critical issues and avoid downtime.
