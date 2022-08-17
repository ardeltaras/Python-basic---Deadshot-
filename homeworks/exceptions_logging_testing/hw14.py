import random
import logging
logging.basicConfig(level=logging.INFO)
from unittest import TestCase


# ------ Exception classes ------ #
class LowBatteryError(Exception):
    def __init__(self):
        self.message = "Low Battery, goes back to charge!"

class FullTrashTankError(Exception):
    def __init__(self):
        self.message = "Full Trash Tank, needs cleanup!"

class EmptyWatterTankError(Exception):
    def __init__(self):
        self.message = "Empty Watter Tank, needs add water!"


# ------ Main class ------ #
class VacuumCleaner:
    volume_trash_tank = 1500
    volume_water_tank = 800

    def __init__(self, trash_tank: int, water_tank: int, battery: int, serial_number):
        self.trash_tank = trash_tank
        if trash_tank < 0 or trash_tank > self.volume_trash_tank:
            raise ValueError
        self.water_tank = water_tank
        if water_tank < 0 or water_tank > self.volume_water_tank:
            raise ValueError
        self.battery = battery
        if battery < 0 or battery > 100:
            raise ValueError
        self.serial_number = serial_number

    @property
    def info(self):
        return {
            "sn": self.serial_number,
            "power": f"{self.battery / 100 :.0%}",
            "water_tank": f"{self.water_tank / self.volume_water_tank:.0%}",
            "trash_tank": f"{self.trash_tank / self.volume_trash_tank:.0%}"}

    def status_battery(self):
        if self.battery < 5:
            self.battery = 0
            raise LowBatteryError
        else:
            self.battery -= 2

    def status_trash_tank(self):
        add_trash = random.randint(0, 20)
        if self.trash_tank == self.volume_trash_tank:
            raise FullTrashTankError
        elif self.trash_tank != self.volume_trash_tank \
                and self.trash_tank + add_trash >= self.volume_trash_tank:
            self.trash_tank = self.volume_trash_tank
        else:
            self.trash_tank += add_trash

    def wet_cleaning(self):
        if self.water_tank == 0:
            raise EmptyWatterTankError
        elif self.water_tank > 0:
            self.water_tank -= 20
            if self.water_tank < 0:
                self.water_tank = 0
                raise EmptyWatterTankError

    def start_cleaning(self, wet_cleaning: bool, time: int):
        logging.info(f"{self.info} STARTED CLEANING")
        try:
            for i in range(time):
                self.status_battery()
                self.status_trash_tank()
            if wet_cleaning:
                self.wet_cleaning()
        except LowBatteryError:
            logging.error("LowBatteryError")
            logging.info(f"{self.info} STOPPED CLEANING")
            return False
        except FullTrashTankError:
            logging.error("FullTrashTankError")
            logging.info(f"{self.info} STOPPED CLEANING")
            return False
        except EmptyWatterTankError:
            logging.error("EmptyWatterTank")
            return False
        logging.info(f"{self.info} FINISHED CLEANING")
        return True

irobot = VacuumCleaner(serial_number="VR-12345",
                       battery=64,
                       water_tank=45,
                       trash_tank=935)
print(f"Info irobot: {irobot.info}")
print(irobot.start_cleaning(True, 20))


# ------ Test class ------ #
class TestVacuumCleaner(TestCase):
    """тест-кейси які потрібно перевірити"""
    def setUp(self) -> None:
        self.test_irobot = VacuumCleaner(serial_number="VR-12345",
                                         battery=54,
                                         water_tank=350,
                                         trash_tank=1050)
        print(f"Info test_irobot: {self.test_irobot.info}")

    """1. повне прибирання на яке вистачає ресурсів"""
    def test_full_cleaning(self):
        self.assertTrue(self.test_irobot.start_cleaning(wet_cleaning=True, time=25))

    """2. прибирання без вологого прибирання на яке вистачає ресурсів"""
    def test_dry_cleaning(self):
        self.assertTrue(self.test_irobot.start_cleaning(wet_cleaning=False, time=25))

    """3. прибирання під час якого не вистачило заряду батареї"""
    def test_low_battery(self):
        self.test_irobot.battery = 30
        self.assertFalse(self.test_irobot.start_cleaning(wet_cleaning=True, time=25))
        self.assertEqual(self.test_irobot.battery, 0)

    """4. прибирання під час якого заповнився сміттє бак"""
    def test_full_trash_tank(self):
        self.test_irobot.trash_tank = self.test_irobot.volume_trash_tank - 100
        self.assertFalse(self.test_irobot.start_cleaning(wet_cleaning=True, time=25))
        self.assertEqual(self.test_irobot.trash_tank, self.test_irobot.volume_trash_tank)

    """5. прибирання під час якого не вистачило води"""
    def test_empty_water_tank(self):
        self.test_irobot.water_tank = 10
        self.assertFalse(self.test_irobot.start_cleaning(wet_cleaning=True, time=25))
        self.assertEqual(self.test_irobot.water_tank, 0)

    """6. проперті info повертає правильне значення"""
    def test_info_property(self):
        res = {'sn': 'VR-12345', 'power': '54%', 'water_tank': '44%', 'trash_tank': '70%'}
        self.assertEqual(self.test_irobot.info, res)

class TestCreateObj(TestCase):
    def test_trash_tank_field(self):
        with self.assertRaises(ValueError):
            test_irobot = VacuumCleaner(serial_number="VR-12345",
                                        battery=54,
                                        water_tank=350,
                                        trash_tank=1501)
            print(test_irobot.info)

    def test_water_tank_field(self):
        with self.assertRaises(ValueError):
            test_irobot = VacuumCleaner(serial_number="VR-12345",
                                        battery=54,
                                        water_tank=801,
                                        trash_tank=1050)
            print(test_irobot.info)

    def test_battery_field(self):
        with self.assertRaises(ValueError):
            test_irobot = VacuumCleaner(serial_number="VR-12345",
                                        battery=101,
                                        water_tank=350,
                                        trash_tank=1050)
            print(test_irobot.info)
