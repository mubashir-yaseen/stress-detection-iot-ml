import serial

def read_serial_data(port='COM3', baudrate=9600):
    try:
        ser = serial.Serial(port, baudrate, timeout=2)
        line = ser.readline().decode('utf-8').strip()
        ser.close()
        values = line.split(',')
        return {
            'GSR': float(values[0]),
            'PPG': float(values[1]),
            'ECG': float(values[2])
        }
    except Exception as e:
        print(f"Error reading serial: {e}")
        return None
