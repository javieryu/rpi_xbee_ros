# My notes for setting up the XBee system

## Testing and configuring XBees with XCTU: https://www.digi.com/resources/documentation/digidocs/pdfs/90001526.pdf

## The hardware that I am using

- Raspberry Pi 4B (w/ power supplies)
- XBee S2C DigiMesh Startup Kit
- 2x microSD cards (128 GB)
- GS305 network switch
- 3x ethernet cables (2x rpi to switch, 1x switch to laptop)

## Setting up RPis

For the sake of making testing and development easier the Raspberry Pis are connected using a local wired network. This way its easy to SSH into each one to run code, and later on to maintain global parameter topics etc. The following is an amalgamation of guides I used to start prepare the Raspberry Pis for use.

### On a machine with ubuntu

- Download and use `rpi-imager` to write the full version of Raspian to a microSD card.
- Create a file `ssh` in the boot partition of the SD card.
- Connect the RPi with an ethernet cable (if stuck on connecting, change the iPv4/6 configs to "shared to other computers").
- Use `arp -na | grep dc:a6:32` to find the RPi's ID address (you may need to `apt install net-tools`).
- Connect to the RPi with `ssh pi@<ip address>` default password is `raspberry`.

### Basic configuration after SSHing

- Keeping the default user: `pi`
- Configuring new password with: `passwd`
- Configure the timezone etc with `sudo raspi-config`
- Set a new hostname with `raspi-config` (since we are working with multiple rpi's we want them to be identifiable).

### Setting up `avahi-daemon` to make SSHing easier (from https://elinux.org/RPi_Advanced_Setup)

- `sudo apt install avahi-daemon` (this is probably unnecessary since its pre-installed on RPi OS)
- `sudo update-rc.d avahi-daemon defaults`
- Create a config file `/etc/avahi/services/multiple.serivce` containing:

```
<?xml version="1.0" standalone='no'?>
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
        <name replace-wildcards="yes">%h</name>
        <service>
                <type>_device-info._tcp</type>
                <port>0</port>
                <txt-record>model=RackMac</txt-record>
        </service>
        <service>
                <type>_ssh._tcp</type>
                <port>22</port>
        </service>
</service-group>
```

- Run `sudo /etc/init.d/avahi-daemon restart` to apply the configuration.
- Should now be able to disconnect and reconnect with `ssh pi@<hostname>.local`

### Setting up Docker

- SSH to the RPi
- Download the Docker install script `curl -fsSL https://get.docker.com -o get-docker.sh`
- Add user to the docker group `sudo usermod -aG docker pi`
- Restart the RPi `sudo shutdown -r now`
- SSH again, and `docker run hello-world` to test the install
