pipeline {
    agent { 
                label 'agent1'
            }
    stages {
        stage('PyTest') { 
            agent { 
                label 'agent1'
            }  
            steps {
                git branch: 'HomePage', url: 'https://github.com/AsadS95x/volunteerfundamentals.git'
                sh '''#!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                cat requirements.txt
                pip3 install -r requirements.txt
                python3 -m pytest --cov=application'''
            }
        }
        stage('Deploy') { 
            agent { 
                label 'agent1'
            }
            steps {
                sh '''#!/bin/bash
                if [ -f  /tmp/gpidfile ]
                  then kill $(cat /tmp/gpidfile)
                fi
                source venv/bin/activate
                JENKINS_NODE_COOKIE=nokill python3 -m gunicorn application:app -D -w 4 -b 0.0.0.0:5000 -p gunicornpidifle'''
            }
        }

    }
}