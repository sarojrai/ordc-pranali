#!/usr/bin/env bash
AUTH_BRANCH="dev"
AUCTION_BRANCH="dev"
WORKING_DIR=$PWD
echo $WORKING_DIR

clone_repos() {
        echo "***************** starting to clone repos *****************"
        # Auth Branch
        git clone -b ${AUTH_BRANCH} https://guptaka691@bitbucket.org/guptaka691/ordc-auth.git || echo "Already Repo. exist!"
        sleep 3
        # Auction Repo
        git clone -b ${AUCTION_BRANCH} https://ordcinfo@bitbucket.org/ordcinfo/reverse-auction.git || echo "Already Repo. exist!"
        sleep 3
        echo "***************** cloned required repos *****************"
}

create_final_dir_structure() {
        echo "***************** copying all the code to codebase dir *****************"
        mkdir ${WORKING_DIR}/codebase
        cp -r ordc-auth/* ${WORKING_DIR}/codebase/
        cp -r reverse-auction/ordc/apps/* ${WORKING_DIR}/codebase/ordc/apps
        cp -r reverse-auction/ordc/dependencies/ra_prerequisite.py ${WORKING_DIR}/codebase/ordc/dependencies
        #rm -rf  .git
        echo "***************** copied all the code to codebase dir *****************"
}

start_server(){
        cd ${WORKING_DIR}/codebase/ordc
        echo "Server trying to start ....................", $PWD
        sleep 5
        nohup python manage.py runserver &
        echo "Server has been started ...................."
}

## call Functions
clone_repos ## Clone git repos on working machine
sleep 1
create_final_dir_structure ## create temprory working folder
sleep 2
start_server