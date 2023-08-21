pipeline{
    agent{
        label : 'RappsDesktop11'

    }

// Where all the work actually happen
    stages {
        stage("build"){
            steps{
                echo 'building the application ...'

            }
        }

        stage("test"){
            steps{
                echo 'testing the application ...'
                
            }
        }

        stage("deploy"){
            steps{
                echo 'deploying the application ...'
            }
        }
    }
}