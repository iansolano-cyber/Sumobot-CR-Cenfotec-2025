from machine import I2C, Pin
import struct
import config

i2c = I2C(
    config.I2C_ID,
    scl=Pin(config.I2C_SCL),
    sda=Pin(config.I2C_SDA),
    freq=config.I2C_FREQ
)

ADDRESS = config.LSM6DS3_ADDRESS

CTRL1_XL = 0x10
CTRL2_G = 0x11

OUTX_L_G = 0x22
OUTX_L_XL = 0x28


def init():

    # Acelerómetro 416 Hz ±2g
    i2c.writeto_mem(ADDRESS, CTRL1_XL, b'\x60')

    # Giroscopio 416 Hz ±245 dps
    i2c.writeto_mem(ADDRESS, CTRL2_G, b'\x60')


def read_vector(register):

    data = i2c.readfrom_mem(ADDRESS, register, 6)

    x = struct.unpack("<h", data[0:2])[0]
    y = struct.unpack("<h", data[2:4])[0]
    z = struct.unpack("<h", data[4:6])[0]

    return x, y, z


def accelerometer():

    x, y, z = read_vector(OUTX_L_XL)

    x = x * 0.061 / 1000
    y = y * 0.061 / 1000
    z = z * 0.061 / 1000

    return x, y, z


def gyroscope():

    x, y, z = read_vector(OUTX_L_G)

    x = x * 8.75
    y = y * 8.75
    z = z * 8.75

    return x, y, z


def gyro_z():

    _, _, z = gyroscope()

    return z


def print_accelerometer():

    x, y, z = accelerometer()

    print(
        "Acelerómetro",
        round(x, 2),
        round(y, 2),
        round(z, 2)
    )


def print_gyroscope():

    x, y, z = gyroscope()

    print(
        "Giroscopio",
        round(x, 2),
        round(y, 2),
        round(z, 2)
    )


def print_all():

    ax, ay, az = accelerometer()
    gx, gy, gz = gyroscope()

    print(
        "ACC:",
        round(ax, 2),
        round(ay, 2),
        round(az, 2)
    )

    print(
        "GYR:",
        round(gx, 2),
        round(gy, 2),
        round(gz, 2)
    )
