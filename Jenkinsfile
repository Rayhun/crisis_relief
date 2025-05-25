pipeline {
    agent any

    environment {
        PROJECT_DIR = '/opt/crisis_relief'
        VENV_PATH = "${PROJECT_DIR}/venv/bin/activate"
    }

    triggers {
        githubPush()  // Enables auto-deploy from GitHub webhook
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'git@github.com:Rayhun/crisis_relief.git',
                    credentialsId: 'e164086c-d5e2-4b41-9c3f-9fd47794271e'
            }
        }

        stage('Install Requirements') {
            steps {
                sh """
                cd ${PROJECT_DIR}
                source ${VENV_PATH}
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Migrations & Collect Static') {
            steps {
                sh """
                cd ${PROJECT_DIR}
                source ${VENV_PATH}
                python manage.py migrate
                python manage.py collectstatic --noinput
                """
            }
        }

        stage('Restart Gunicorn') {
            steps {
                sh 'sudo systemctl restart crisis_relief'
            }
        }
    }
}
