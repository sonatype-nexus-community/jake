/*
 * Copyright 2019-Present Sonatype Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

@Library(['private-pipeline-library', 'jenkins-shared']) _

dockerizedBuildPipeline(
  buildAndTest: {
    sh '''
    # development only requirements
    pip3 install -r requirements-dev.txt
    python -m xmlrunner discover -o test-results/
    # hot mess to uninstall dev requirements before we self scan. probably should move to pipenv
    pip3 uninstall -r requirements-dev.txt -y
    '''
  },
  deployBranch: 'main',
  vulnerabilityScan: {
    withDockerImage(env.DOCKER_IMAGE_ID, {
      withCredentials([usernamePassword(credentialsId: 'policy.s integration account',
        usernameVariable: 'IQ_USERNAME', passwordVariable: 'IQ_PASSWORD')]) {
        sh '''
        python setup.py bdist_wheel
        cd dist && WHEEL_NAME=$(ls -1) && cd ..
        pip install --user dist/$WHEEL_NAME
        jake iq --application jake --stage stage-release --user $IQ_USERNAME --password $IQ_PASSWORD --host https://policy.ci.sonatype.dev        
        #jake iq --application jake --stage stage-release --user $IQ_USERNAME --password $IQ_PASSWORD --host https://policy.ci.sonatype.dev || export jakeFailed=true        
        #cat ${HOME}/.ossindex/jake.combined.log
        '''
      }
    })
  },
  onSuccess: {
    githubStatusUpdate('success')
  },
  onFailure: {
    githubStatusUpdate('failure')
    notifyChat(currentBuild: currentBuild, env: env, room: 'community-oss-fun')
    sendEmailNotification(currentBuild, env, [], 'community-group@sonatype.com')
  }
)
