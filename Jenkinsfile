pipeline {
  environment {
    registry = 'tejunlee007/screening-test-backend'
    registryCredential = 'dockerhub'
    backendImage = ''
  }
  agent none
  stages {
    stage('build') {
      agent any
      steps {
        sh './build.sh'
      }
    }
    stage('test') {
      agent {
        docker {
          image 'python:3.6.5'
        }
      }
      environment {
        PYTHONUNBUFFERED = '1'
        PATH = '$PATH:/backend'
        PYTHONPATH = '$PYTHONPATH:/:/backend'
        CI = 'true'
      }
      steps {
        sh './test.sh'
      }
    }
    stage('push') {
      agent any
      steps {
        sh  './push.sh'
      }
    }
    stage('deploy') {
      agent any
      steps {
        sh  './push.sh'
      }
    }
  }
}
