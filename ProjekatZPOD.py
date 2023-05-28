import pywinusb.hid as hid

def save_usb_info_to_file(file_path, usb_info):
    with open(file_path, 'a') as file:
        file.write("------------------------------\n")
        file.write("Device ID: {}\n".format(usb_info['device_id']))
        file.write("Manufacturer: {}\n".format(usb_info['manufacturer']))
        file.write("Product: {}\n".format(usb_info['product']))
        file.write("Serial Number: {}\n".format(usb_info['serial_number']))
        file.write("------------------------------\n")

def main():
    # Definišite putanju do tekstualnog dokumenta
    file_path = 'Podaci.txt'

    # Pronađi sve USB HID uređaje
    all_devices = hid.find_all_hid_devices()

    # Set za praćenje već prikazanih uređaja
    shown_devices = set()

    for device in all_devices:
        device_id = device.product_id

        # Proveri da li je uređaj već prikazan
        if device_id in shown_devices:
            continue

        # Dodaj uređaj u set prikazanih uređaja
        shown_devices.add(device_id)

        # Prikupi informacije o uređaju
        manufacturer = device.vendor_name
        product = device.product_name
        serial_number = device.serial_number

        # Sačuvaj informacije o USB uređaju u tekstualni dokument
        usb_info = {
            'device_id': device_id,
            'manufacturer': manufacturer,
            'product': product,
            'serial_number': serial_number,
            
        }
        save_usb_info_to_file(file_path, usb_info)

if __name__ == '__main__':
    main()
