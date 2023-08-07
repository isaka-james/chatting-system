# chatting-network system

This is the system in which two devices can chat and sending and receiving files via **ip-address**  using **TCP** connection. I have managed well such that It can be used within a **localhost**.

This contains two files which are **server-side.py** and **client-side.py**.

# Installation 

The installation will be of two sides server and client respectively!!. I assumed that the user **root@mastermind:#** is the server and **root@blackhat:#** is the client. Even if it is viceversa it will anyway works.

- Remember that we will be using **socket** module and other system-built modules. Hence if you don't have in your machine it is necessary to install it. It does not depend you are client or server all of you must have the file.
```bash
root@masterplan:# pip install socket
```

Firstly on the **server-side**
```bash
root@masterplan:# git clone https://github.com/MrNkolima/chatting-system
root@masterplan:# cd chatting-system
root@masterplan:# python3 server-side.py
Enter your server Address:: 172.80.25.80      # <---- Here write your ip address
```
- If you want to test in a local machine then you can also hit **enter** without typing the **ip-address**

Secondly on the **client-side.py**
```bash
root@masterplan:# git clone https://github.com/MrNkolima/chatting-system
root@masterplan:# cd chatting-system
root@masterplan:# python3 server-side.py
Write a Server address:: 172.80.25.80      # <---- Here write server address
```
- If you are testing this in the local machine then no need to **git cloning** the secong time. Just open a new session and run the **client-side.py**
- Also if you are testing on local machine then you can hit enter on **Write a Server address::** without filling.
- Also it works if you type **localhost** on the address in both cases if you are testing on the local machine.



## Behind the scenes
  - The port in which the communication will be happening is **5050**.
  - Type **file** in the chatting session to have an option of sending the file.
  - Type **STOPPED** in the chatting session to stop communication.
  - On the server side type **quit** to turn off the server.


# PRO & CONS
- [x] The chatting is safe since I configured the server to listen only **one** user.
- [x] The files can be transfered.
- [ ] The files transported are limited to 5MB but you can change by changing the buffersize variable.
- [ ] The files which are allowed to be transfered are text-based images and not other files like images, audio, pdf, zip and videos. But all the remained type of files are supported!!.
- [ ] The chatting relie on sending each other files or texts and you cannot send message consecutive without an incoming message, hence it look like send to receive and vice versa is true.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


Please make sure to update tests as appropriate.


## Free to use

- You can use this for free either by modifying it or use as it is.
