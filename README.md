# RaspiPicoWPy
For: Raspi Pico W; in: Python (Micropython); File Transfer within WLAN; (vs2: SPI File from Interface)

This projects target: Microcontroller Raspberry Pi Pico W (2022).
Firmware: https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2
(Which is: micropython)

I can't recommend a project setup.
(W11 (disabled thonny): Python3.10, Visual C++ 13 (via MS BuildTools some big Python Desktop SDK libraries to add) plus Thonny to move code to target)
(with pip install micropy, micropy-cli; git clone https://github.com/cpwood/Pico-Stub; 
 micropy stubs add Pico-Stub-main/dist/micropy-cli/;
 pip install pylint; - *did not end in a proper lint-ing of micropy syntax unfortunalety.*
 micropy init <projectName> OR clone this;
 VSCode plugins are missing.)
 
This shall enable Pico to communicate in WLAN (as do_connect()).
Use ussl.socket to upload a file to a dedicated ftp-like Server - configured in secrets.py.
Inspiration for server is: 
https://github.com/justEhmadSaeed/Python-Sockets-File-Transfer
