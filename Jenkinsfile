pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {
                git branch: 'HomePage', url: 'https://github.com/AsadS95x/volunteerfundamentals.git'
                sh '''#!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                sudo apt-get install python3-pip
                pip3 install -r requirements.txt
                python3 -m create.py'''
            }
        }
        stage('PyTest') { 
            steps {
                git branch: 'HomePage', url: 'https://github.com/AsadS95x/volunteerfundamentals.git'
                sh '''#!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                pip3 install -r requirements.txt
                python3 -m pytest --cov=application'''
            }
        }
        stage('Deploy') { 
            steps {
                sh '''#!/bin/bash
                if [ -f  /tmp/gpidfile ]
                  then kill $(cat /tmp/gpidfile)
                fi
                source venv/bin/activate
                JENKINS_NODE_COOKIE=nokill gunicorn application:app -D -w 4 -b 0.0.0.0:5000 -p /tmp/gpidfile'''
            }
        }

    }
}