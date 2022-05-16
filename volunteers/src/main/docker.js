import baseURL from '../renderer/functions/baseURL';

const exec = require('child_process').exec

const Docker = require('dockerode');

const docker = new Docker();

const spinupNewContainer = function () {
    return new Promise((resolve, reject) => {
        docker.createContainer({
            Image: "enigpy",
            Tty: true 
        }).then(async(container) => {
            await container.start();
            resolve(container.id);
        }).catch((reason) => {
            reject(reason);
        })
    })
}

const runPreprocessSetup = function (containerId, zipAccessLink, fileAccessLink, phase, step, token) {
    return new Promise((resolve, reject) => {
        const command = `docker exec  ${containerId} bash fetch-and-setup.sh ${zipAccessLink}`
        const command1 = `docker exec  ${containerId} python3 main.py ${fileAccessLink} ${phase} ${step} ${baseURL} ${token}`
        console.log(command)
        console.log(command1)
        exec(command, (err, stdout, stderr) => {
            if(err) {
                reject(err.stack)
                return;
            }
            exec(command1, (err, stdout, stderr) => {
                if(err) {
                    console.log("ERROR 1", err.stack)
                    return;
                }
                console.log("LOG 1", stdout + stderr);
            })
            resolve("LOG 0", stdout + stderr);
        })
        
    })
}

const getAllTasks = function(){
    return new Promise((resolve, reject)=> {
        docker.listContainers(function (err, containers){
            if(err) {
                reject(err)
                return
            }
            const data = []
            for(var i=0; i<containers.length; i++){
                data.push({
                    "name" : containers[i].Names[0].replace("/", "").replace("_", " "),
                    "status" : containers[i].Status,
                })
            }
            resolve(data)
        })
    })
}


// runPreprocessSetup("4d2253edf98e", "https://drive.google.com/uc?export=download&id=1hQTpEbty80Z0nxI-wJPfDlqLtWRnengY")

export {
    spinupNewContainer,
    runPreprocessSetup,
    getAllTasks
}
