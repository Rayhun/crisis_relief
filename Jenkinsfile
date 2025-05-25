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
                    url: 'https://github.com/Rayhun/crisis_relief.git',
                    credentialsId: 'c936b724-36bd-49a8-a46a-ea2fd030daa1'
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
