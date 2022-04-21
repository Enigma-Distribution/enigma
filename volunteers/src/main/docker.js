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

const runPreprocessSetup = function (containerId, zipAccessLink) {
    return new Promise((resolve, reject) => {
        const container = docker.getContainer(containerId);
        console.log("container->",container)
        container.exec({
            Env: ['ZIP_ACCESS_LINK='+"https://drive.google.com/uc?export=download&id=1hOZI5kx-z0CBkh4Ved3FSQ6P6vBdOizn"],
            AttachStdout: true,
            AttachStderr: true,
            Tty: true,
            // Cmd: [`mkdir`, `testihng123`]
            Cmd: [`source`, `fetch-and-setup.sh`]
        }).then((execCommand) => {
            console.log("Exec Command", execCommand)
            execCommand.start({ hijack: true, stdin: false },  function(err, stream) {
                stream.setEncoding('utf8');
              const container_output=(stream.pipe(process.stdout));
              console.log("Directory in container is" ,container_output)
              })
        }).catch((reason) => {
            console.log("Rejected Value", reason);
            reject(reason);
        })
    })
}

const fetchAndRun = function (containerId, {fileAccessLink, phase, step}) {
    return new Promise((resolve, reject) => {
        const container = docker.getContainer(containerId);
        container.exec({
            Env: [`ENIGMA_FAE="${fileAccessLink}"`, `PHASE=${phase}`, `STEP=${step}`, `SERVER_URL=${baseURL}`],
            Cmd: ['python3 main.py']
        }).then((exec) => {
            exec.start().then((value) => {
                resolve(value);
            });
        }).catch((reason) => {
            reject(reason);
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
    fetchAndRun,
    getAllTasks
}
