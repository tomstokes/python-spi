# python-spi

**Note:** python-spi is still a work in progress.

## Overview

A pure Python SPI interface using the Linux spidev device

## Features

- Pure Python implementation. No C module to compile.
- Supports half-duplex reads and writes as well as full-duplex transfers.
- Exposes all available spidev interface options as properties.

## Example

    import spi
    spi = SPI("/dev/spidev1.0")
    spi.mode = SPI.MODE_0
    spi.bits_per_word = 8
    spi.speed = 500000
    received = spi.transfer("\xAA\xBB\xCC")
    spi.write("\x00\x11\x22")
    received = spi.read(10)



