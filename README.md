# python3-spi

Python 3.x interface for SPI communications using Linux spidev

This is a fork of https://github.com/tomstokes/python-spi which seems to be abandoned with the python 3 compatibility patch proposed by Tom Egan applied.

## Features

- Pure Python implementation. No C module to compile.
- Supports half-duplex reads and writes as well as full-duplex transfers.
- Exposes all available spidev interface options as properties.

## Requirements

- spidev enabled in the kernel and (if necessary) the device tree.
- Write permissions to the /dev/spidevN.N device.
  - Some distributions have an 'spi' group for this purpose. If available, add this group to the user account and ensure the spidev device is group-writeable.
  - If no 'spi' group exists, a udev rule can be created to set the permissions of the spidev device.
  - As a last resort, running the python script as root should allow access to the spidev. **Note** This is not recommended. Use the 'spi' group or udev rules whenever possible.

## Example
```python3
import spi
spi = SPI("/dev/spidev1.0")
spi.mode = SPI.MODE_0
spi.bits_per_word = 8
spi.speed = 500000
received = spi.transfer([0x11, 0x22, 0xFF])
spi.write([0x12, 0x34, 0xAB, 0xCD])
received = spi.read(10)
```
