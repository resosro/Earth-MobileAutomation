pipeline{
    agent{
        label 'RAppsDesktop11'
    }

// Must use params. in order to use the parameters here, 
// This essentially allows for different configurations of the job
    parameters{
        string(name : 'VERSION', defaultValue: '', description: 'version to deploy on prod')
        choice(name : 'VERSION', choices: ['1.1.0', '1.2.0'], description: '')
        booleanParam(name : 'executeTests', defaultValue: true, description: '')
    }
    environment{
        NEW_VERSION = '1.3.0'
        SERVER_CREDENTIALS = credentials('')
    }

// Where all the work actually happens, does certain things like in jenkins UI
    stages {
        stage("build"){
            steps{
                echo 'building the application ...'
                //if you want the string to be formatted it must use ""
                echo "building version ${NEW_VERSION}"
            }
        }

        stage("test"){
            when{
                expression{
                    params.executeTests
                }
            }

            steps{
                echo 'testing the application ...'
                echo "${params.executeTests}"
                
            }
        }

        stage("deploy"){
            steps{
                echo 'deploying the application ...'
                withCredentials([
                    usernamePassword('server-credentials', usernameVariable : USER, usernamePassword: PWD)
                ]){
                    sh "some script ${USER} ${PWD}"
                }
            }
        }
    }

    
    // for reporting build status/status changes
    // post{
    //     always{

    //     }
    //     success{

    //     }
    //     failure{

    //     }

    // }
}