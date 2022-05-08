import { container } from 'webpack';
import baseURL from '../renderer/functions/baseURL';

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

const runPreprocessSetup = function (containerId, {zipAccessLink, fileAccessLink, phase, step, token}) {
    return new Promise((resolve, reject) => {
        const container = docker.getContainer(containerId);
        container.exec({
            AttachStdout: true,
            Tty: true,
            Cmd: [`bash`, `fetch-and-setup.sh`, `${zipAccessLink}`,`${fileAccessLink}`, `${phase}`, `${step}`, `${baseURL}`, `${token}`, `>`, `log`]
        }).then((execCommand) => {
            execCommand.start().then((value) => {
                resolve(value);
            });
        }).catch((reason) => {
            reject(reason);
        })
    })
}

// const fetchAndRun = function (containerId, {fileAccessLink, phase, step, token}) {
//     return new Promise((resolve, reject) => {
//         const container = docker.getContainer(containerId);
//         console.log("fetchandrun")
//         console.log("Printing values")
//         console.log(fileAccessLink, phase, step, baseURL, token)
//         console.log(`python3 main.py ${fileAccessLink} ${phase} ${step} ${baseURL} ${token}`)
//         container.exec({
//             // AttachStdout: true,
//             // Tty: true,
//             // Env: [`ENIGMA_FAE=${fileAccessLink}`, `PHASE=${phase}`, `STEP_ID=${step}`, `API_URL=${baseURL}`, `AUTH_TOKEN=${token}`],
//             Cmd: [`python3`, `main.py`, `ENIGMA_FAE=${fileAccessLink}`, `PHASE=${phase}`, `STEP_ID=${step}`, `API_URL=${baseURL}`, `AUTH_TOKEN=${token}`]
//         }).then((exec) => {
//             exec.start().then((value) => {
//                 resolve(value);
//             });
//         }).catch((reason) => {
//             reject(reason);
//         })
//     })
// }

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
    fetchAndRun,
    getAllTasks
}
