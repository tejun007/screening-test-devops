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
        sh '''
            cd /var/jenkins_home/workspace/screening-test-devops_master/backend
            pip install --trusted-host pypi.python.org -r requirements.txt
           '''
      }
    }
    stage('test') {
      steps {
        sh 'pytest backend'
      }
    }
  }
  environment {
    PYTHONUNBUFFERED = '1'
    PATH = '$PATH:/backend'
    PYTHONPATH = '$PYTHONPATH:/:/backend'
  }
}
