# The users in the group interns should be able to login via private key, and not a password.
Generated the key using ```ssh``` command ```ssh-keygen```.
SSh keygen generates two types of keys public key and private key. And we have to copy public key. So type the followimg command.
```
ssh-copy-id -i ~/.ssh/id_rsa.pub hostname@your-server-ip

ssh-copy-id -i ~/.ssh/id_rsa.pub mehul-intern@192.168.176.254
```
That's it now you can login by using ```ssh mehul-intern@192.168.176.254```

<img src="https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week1/output_images/ssh.png">
