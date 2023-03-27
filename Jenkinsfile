pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
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