# QNAP Lcd Info 📺

Welcome to the **QNAP Lcd Info** project! \
It allows you to easily use the screen of your QNAP with Linux. You can run the script manually, as a system service, or as a script for TrueNAS SCALE.

## Features 🚀

- **Disable "System Booting" Message**: Automatically turns off the default "System Booting..." message.
- **Display System Information**: Shows CPU, RAM, disk usage, and IP addresses.
- **Interactive Navigation**: Navigate through the displayed information using buttons.
- **Screen Timeout**: Automatically turns off the screen when not in use.

## Compatible Devices ✅

This utility has been tested and is confirmed to work on the following device:

- **QNAP TS-453**
- **QNAP TS-453 PRO**

## Installation and Usage 📦

### Manual Execution
1. Install Python & git:
```sh
   sudo apt install python3 python3-pip git -y
```
2. Clone this repository to your local machine:
```sh
   git clone https://github.com/iwurui/QnapLcdInfo.git
   cd QnapLcdInfo
```
3. Install requirements:
```sh
   sudo pip3 install -r requirements.txt
```
4. Run script:
```sh
   chmod 775 lcdInfo.py
    ./lcdInfo.py
```

### As a Systemd Service

Before proceeding, make sure to run all the commands from the Manual Execution section and test that everything is working correctly.

1. Once you have verified that the script works, run the following command:
```sh
   bash ./install_service.sh
   ```

### TrueNAS SCALE Script
To run the script on TrueNAS, simply execute or schedule the following script at startup:
```sh
wget -qO- https://raw.githubusercontent.com/mpeirone/QnapLcdInfo/main/run_truenas.sh | sudo bash
```

## Support ⭐

If you find this project useful, please consider giving it a star on GitHub. Your support is greatly appreciated and helps us improve the project!

## Contributing 🤝

We welcome contributions to improve this project! Here are some ways you can help:

- Report bugs and suggest features by opening an issue.
- Submit pull requests to fix issues or add new features.
- Improve documentation and examples.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements 🙌

Thanks to all the contributors and the open-source community for their support and collaboration.
