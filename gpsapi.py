import subprocess
import os


class GpsApi():
    def __init__(self, nox_adb_path: str) -> None:
        if not os.path.exists(nox_adb_path):
            raise FileExistsError(f"文件不存在：{nox_adb_path}")

        self.nox_adb_path = nox_adb_path

    def start_service(self):
        output = self._adbcmd('devices')
        lines = [p for p in output.splitlines(keepends=False) if p != '']
        output = '\n'.join(lines)
        print("<adb>")
        print(output)
        print("</adb>")

        if '127.0.0.1' not in output:
            print("[WARNING] device may not be connected")

    def _adbcmd(self, command: str):
        outb = subprocess.check_output(f"{self.nox_adb_path} {command}")
        return outb.decode()

    def set_position(self, pos):
        self.set_longitude(pos[0])
        self.set_latitude(pos[1])

    def set_longitude(self, longitude: float):
        """
        设置经度
        """
        output = self._adbcmd(
            f'shell setprop persist.nox.gps.longitude {longitude}')
        return output

    def set_latitude(self, latitude: float):
        """
        设置纬度
        """
        output = self._adbcmd(
            f'shell setprop persist.nox.gps.latitude {latitude}')
        return output
