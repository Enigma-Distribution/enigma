# This script fetched the zip file containing code from CDN, unzips it, places it to correct location,
# cleans up unnecessary zip file, and finally, if setup file exists, runs the file.

ZIP_ACCESS_LINK=$1

if [[ $ZIP_ACCESS_LINK ]]
then
    wget $ZIP_ACCESS_LINK -O zipClient

    mkdir client

    unzip zipClient -d client

    rm zipClient

    # touch data.json

    # echo "{}" >> data.json

    if [ -e client/setup.sh ]
    then
        source client/setup.sh
    fi
else
    echo "No Zip Access Link Found! Quitting..."
fi