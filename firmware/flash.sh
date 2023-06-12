# flash micropython
read -p "bring GPIO0 low, reset device, and press enter"
esptool.py --port /dev/ttyUSB0 erase_flash
read -p "bring GPIO0 low, reset device, and press enter"
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect --verify -fm dio 0x0 ./microhomie-esp8266-v3.0.2.bin
read -p "reset device and press enter"
# upload files
echo "sleeping"
sleep 5
echo "putting files on device"
ampy -p /dev/ttyUSB0 put main.py
ampy -p /dev/ttyUSB0 put settings.py
ampy -p /dev/ttyUSB0 put hpm.py
read -p "reset device and press enter"
echo "done!"
