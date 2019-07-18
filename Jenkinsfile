pipeline {
  agent {
    docker {
      image 'python:3.6.5'
      args '-p 5000:5000'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'pip install --trusted-host pypi.python.org -r ./backend/requirements.txt'
      }
    }
    stage('test') {
      environment {
        CI = 'true'
      }
      steps {
        sh 'pytest ./backend'
      }
    }
    stage('deploy') {
      steps {
        sh '''docker-compose up -d
docker-compose ps
docker-compose down --volumes
docker-compose push'''
      }
    }
  }
  environment {
    PYTHONUNBUFFERED = '1'
    PATH = '$PATH:/backend'
    PYTHONPATH = '$PYTHONPATH:/:/backend'
  }
}