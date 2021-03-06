<p align="center"
<img src ="" width = 200px>
</p>

<h2 align = 'center'> Enigma.
</h2>

<p align='center'>
Distributed computing solution for a world full of volunteers. Enigma  uses  the  power  of  Map-Reduce and Docker  to  leverage  unused  CPU  cycles  of  computers 
owned by people and acts as a bridge between developers and users.
</p>

<div align="center">

[![](https://img.shields.io/badge/Made_with-Flask-blue?style=for-the-badge&logo=Flask)](https://flask.palletsprojects.com/en/1.1.x/) 
[![](https://img.shields.io/badge/Made_with-PostgreSQL-blue?style=for-the-badge&logo=PostgreSQL)](https://www.postgresql.org/docs/current/)
[![](https://img.shields.io/badge/Made_with-Docker-blue?style=for-the-badge&logo=Docker)](https://docs.docker.com/get-started/overview/)
[![](https://img.shields.io/badge/IDE-Visual_Studio_Code-blue?style=for-the-badge&logo=visual-studio-code)](https://code.visualstudio.com/ "Visual Studio Code")

</div>

-----------------------------------

### System Design
<p align="center">
<img src ="https://github.com/Enigma-Distribution/enigma/blob/main/assets/System%20Architecture.jpg" width = 500px height=350px >
</p>


-----------------------------------

### Low Level Server Design
<p align="center">
<img src ="https://github.com/Enigma-Distribution/enigma/blob/main/assets/Low%20Level%20Server%20Design.jpg" width = 500px>
</p>


-----------------------------------

### Queuing System
<p align="center">
<img src ="https://github.com/Enigma-Distribution/enigma/blob/main/assets/Queuing%20System.jpg" width = 500px>
</p>


-----------------------------------
###             Live Demo
`Client`: <a href="https://the-enigma.netlify.app/">https://the-enigma.netlify.app/<a/> <br>
`Backend` : <a href="https://enigma-webapp.herokuapp.com/">https://enigma-webapp.herokuapp.com/<a/>  <br>
`Project Report` : <a href="https://drive.google.com/file/d/1PcTjHCZh7Xdz9qJso1hr1aObMaBaqHFx/view?usp=sharing">Report Link <a/>  <br>
`Video Explanation` : <a href="https://drive.google.com/file/d/1RZ7CUoNWS8H8RtCi0hYofyGcT1v6P9WE/view?usp=sharing">Video Link <a/>  <br>


-----------------------------------
###             ???? Tech stack
`Frontend` : ReactJS <br>
`Backend` : Flask <br>
`Database` : PostgreSQL <br>
`Software` : Docker, NuxtJS, ElectronJS, Python  <br>
  
 
-----------------------------------

### :guide_dog: Installation Guide

A step by step series of examples that tell you how to get a development env running

In your cmd:

```
git clone https://github.com/Enigma-Distribution/enigma.git
cd enigma
```

  
1) For database setup run the content of "database.txt" in pgAdmin 
  - open pgAdmin
  - Create new database "enigma_db"
  - Open query tool and run content of "database.txt". This would create all the necessary tables in database.
  

  
2) For server setup,

```
cd server
pip install -r requirements.txt
```

Create .env file in "server" directory and paste
```
SECRET='SOME@SECRET@321123'
POSTGRESURL='postgres://postgres:postgres@localHost:5432/enigma_db'
BUCKET_NAME="NOT REQUIRED"
aws_access_key_id = "NOT REQUIRED"
aws_secret_access_key = "NOT REQUIRED"
```
Run  
```
  python enigma.py
```

3) For website setup open another terminal,

```
cd enigma
cd public
npm install
npm start
```

You are done with the setup now!

-----------------------------------

### ???? To-do List

- [ ] Implement Proper Credit System wuth Payment gateway. 
- [ ] Add runtime support for Javascript, and other languages.
- [ ] Software Updates. 

------------------------------------------


### :page_with_curl: Acknowledgements & References

- Flask Documentation - https://flask.palletsprojects.com/en/1.1.x/
- ReactJS - https://www.postgresql.org/docs/current/
- Docker - https://docs.docker.com/get-started/overview/
- Electron - https://www.electronjs.org/docs/latest/
- NuxtJS - https://nuxtjs.org/docs/get-started/installation/

-----------------------------------
