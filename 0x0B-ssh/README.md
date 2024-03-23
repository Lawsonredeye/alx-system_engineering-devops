# 0x0B-ssh

SSH also known as secure shell is a way of connecting to a server in another location or conecting to a remote system.
They are a lot of things that comes into play when thinking about ssh and that is the nenefits of SSH.

When working as a DevOps engineer, working with servers might/would/could be your day to day thing, configuring and setting up could also be another thing. Now, these servers are located in other parts of the world and you cant be travelling from one country to another every single time when a server needs updating or some form of system administration and thats where SSH comes in.

With SSH, you can connect to a remote server and access its information as well as its files and databse (if any).
SSH is a powerful tool to work with and theres a lot of things you can do.

## How to connect to a server
1. create your own ssh-keygen
2. copy the public key and send it to the desired server using
`ssh-copy-id -i ~/.ssh/id_rsa.pub user@ipaddress`
