# Preamble

this guide is made assuming you are using linux, if you are not, ask the volunteers, they can guide you on anything that is too different, ( the procedure should generally be mostly the same )

## What is esp32

esp32 is a microcontroller

According to chatgpt:
> A **microcontroller** is a compact integrated circuit designed to govern a specific operation in an embedded system. It typically includes a **processor (CPU), memory (both RAM and ROM), and input/output (I/O) peripherals** all on a single chip. Microcontrollers are used in automatically controlled devices like appliances, automobiles, and various electronic gadgets to perform dedicated tasks.
>
> In short, a microcontroller is a tiny computer on a single chip meant for controlling other devices or systems.
  
### Now, how do we program a microcontroller?  

the most commonly used is [arduino ide](https://www.arduino.cc/en/software/), but it is far from the only option. What we will be using today is [micropython](https://micropython.org/)  

## Pre install steps

first cd to the location where you would like to install all esp files

```bash
cd ~/Documents/
mkdir esp32-oscilloscope-tutorial
cd esp32-oscilloscope-tutorial
```

then we will make a python virtual enviornment so we do not mess up our global enviornment

on linux:

```bash
python -m venv venv
source venv/bin/activate
```

or on windows:

```powershell
python -m venv venv
venv/Scripts/activate.bat
```

## Installing micropython

[**online guide**](https://micropython.org/download/ESP32_GENERIC/)

first we need to install esptool to flash micropython firmware to the esp32

```bash
pip install esptool
esptool --help
```

```bash
curl -O https://micropython.org/resources/firmware/ESP32_GENERIC-UNICORE-20250911-v1.26.1.bin
esptool erase_flash
esptool --baud 460800 write_flash 0x1000 ESP32_GENERIC-UNICORE-20250911-v1.26.1.bin
```

# Explain boot.py and main.py, also follow online guide for how to use if there is time, o\/w

## Installing micropython flashers

there are some great gui options like thonny ide. There are also amazing cli options, like ampy rshell or mpremote

we will be using [thonny ide](https://thonny.org/)
