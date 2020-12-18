# My notes for setting up the XBee system

## Testing and configuring XBees with XCTU: https://www.digi.com/resources/documentation/digidocs/pdfs/90001526.pdf

## The hardware that I am using

- Raspberry Pi 4B (w/ power supplies) (could use a model 3, but it would be slow because we have to use a 64-bit OS)
- XBee S2C DigiMesh Startup Kit
- 2x microSD cards (128 GB)
- GS305 network switch
- 3x ethernet cables (2x rpi to switch, 1x switch to laptop)

## Setting up RPis

For the sake of making testing and development easier the Raspberry Pis are connected using a local wired network. This way its easy to SSH into each one to run code, and later on to maintain global parameter topics etc. The following is an amalgamation of guides I used to start prepare the Raspberry Pis for use.

### On a machine with ubuntu
The version of ROS2 (Foxy) that we are going to use for this project does not have `arm32v7` Docker images so we need a `arm64v8`. To that end we cannot use the typical Raspberry OS (as of writting this) since it is 32-bit. Here we are going to use Ubuntu which I have read is cooperative with ROS2, and has a 64-bit version. Additionally, this entire guide is centered on 64-bit applications, and so a Raspberry Pi 3+/4 or required. 

- Download and use `rpi-imager` to write a Ubuntu 20.04.1 Server Image to a microSD card.
- Connect the RPi with an ethernet cable (if stuck on connecting, change the iPv4/6 configs to "shared to other computers").
- Use `arp -na | grep dc:a6:32` to find the RPi's ID address (you may need to `apt install net-tools`).
- Connect to the RPi with `ssh ubuntu@<ip address>` default password is `ubuntu`.

### Basic configuration after SSHing

- You'll be prompted here to input a new password if this is the first login.
- After you update the password for some reason the Pi with close the connection so ssh again and sign in with the new password.
- Perform the usual software updates: `sudo apt update && sudo apt upgrade`
- Set a new hostname with `hostnamectl set-hostname <new name>` (since we are working with multiple rpi's we want them to be identifiable).

### Setting up `avahi-daemon` to make SSHing easier

- `sudo apt install avahi-daemon`
- `sudo update-rc.d avahi-daemon defaults` (this step might not be necessary, but it kept popping up on tutorials so I do it)
- Should now be able to disconnect and reconnect with `ssh ubuntu@<hostname>.local`

### Installing Docker

- SSH to the RPi
- Download the Docker install script `curl -fsSL https://get.docker.com -o get-docker.sh`
- Run the installation script `sudo sh get-docker.sh`
- Add user to the docker group `sudo usermod -aG docker $USER`
- Restart the RPi `sudo reboot`
- SSH again, and `docker run hello-world` to test the install
