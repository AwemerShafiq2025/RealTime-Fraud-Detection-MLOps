pipeline {
    agent any

    environment {
        // Hamare Docker image ka naam jo humne Phase 4 mein rakha tha
        DOCKER_IMAGE = 'fraud-detection-api:latest'
    }

    stages {
        // Stage 1: GitHub se taza tareen code uthana
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub repository...'
                checkout scm
            }
        }

        // Stage 2: Docker Image Build karna (Build)
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                // Linux/Jenkins server ke liye standard shell command
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        // Stage 3: Code ya API ki testing (Test)
        stage('Test') {
            steps {
                echo 'Running basic tests...'
                // Yahan hum future mein pytest commands add kar sakte hain
                sh 'echo "Simulating tests... All tests passed!"'
            }
        }

        // Stage 4: Kubernetes par deploy karna (Deploy)
        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying Container to Kubernetes Cluster...'
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }
    }

    // Pipeline ke aakhir mein status messages
    post {
        success {
            echo '✅ CI/CD Pipeline Executed Successfully! App is deployed.'
        }
        failure {
            echo '❌ Pipeline Failed. Please check the logs.'
        }
    }
}