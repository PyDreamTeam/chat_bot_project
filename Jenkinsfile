pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Stop and delete old containers') {
      steps {
        sh 'docker-compose down'
        sh 'docker system prune -f'
        // sh 'docker stop $(docker ps -aq) && docker rm $(docker ps -aq)'
      }
    }
    stage('Docker build') {
      steps {
        // Build Docker image 
        sh 'docker-compose build'
      }
    }
    stage('Deploy') {
      steps {
        // Deploy Docker container to a server
        sh 'docker-compose up -d'
      }
    }
  }
}