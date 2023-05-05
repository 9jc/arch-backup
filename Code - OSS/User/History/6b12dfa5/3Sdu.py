
import sys
import atexit
import time
import libtorrent as lt
import time, os
import os.path


# class WindowsConsole:
#     def __init__(self):
#         self.console = Console.getconsole()

#     def clear(self):
#         self.console.page()

#     def write(self, str):
#         self.console.write(str)

#     def sleep_and_input(self, seconds):
#         time.sleep(seconds)
#         if msvcrt.kbhit():
#             return msvcrt.getch()
#         return None


# class UnixConsole:
#     def __init__(self):
#         self.fd = sys.stdin
#         self.old = termios.tcgetattr(self.fd.fileno())
#         new = termios.tcgetattr(self.fd.fileno())
#         new[3] = new[3] & ~termios.ICANON
#         new[6][termios.VTIME] = 0
#         new[6][termios.VMIN] = 1
#         termios.tcsetattr(self.fd.fileno(), termios.TCSADRAIN, new)

#         atexit.register(self._onexit)

#     def _onexit(self):
#         termios.tcsetattr(self.fd.fileno(), termios.TCSADRAIN, self.old)

#     def clear(self):
#         sys.stdout.write('\033[2J\033[0;0H')
#         sys.stdout.flush()

#     def write(self, str):
#         sys.stdout.write(str)
#         sys.stdout.flush()

#     def sleep_and_input(self, seconds):
#         read, __, __ = select.select(
#             [self.fd.fileno()], [], [], seconds)
#         if len(read) > 0:
#             return self.fd.read(1)
#         return None


# if os.name == 'nt':
#     import Console
#     import msvcrt
# else:
#     import termios
#     import select


# def write_line(console, line):
#     console.write(line)

# source:
# https://stackoverflow.com/questions/6051877/loading-magnet-link-using-rasterbar-libtorrent-in-python
#
# ATTENTION: This is only a example of to use a python bind of torrent library in Python for educational purposes.
#            I am not responsible for your download of illegal content or without permission.
#            Please respect the laws license permits of your country.


ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'save_path': '/home/i0xfce/tools/t-stream/src',
    'storage_mode': lt.storage_mode_t(2),
    # 'paused': False,
    # 'auto_managed': True,
    # 'duplicate_is_error': True
    }
# link = "magnet:?xt=urn:btih:C4B4F07937FC2534CF02C1F724D23240793A6FA9&dn=Gordon+Ramsay+Teaches+Cooking+II+-+Elevated+Home+Recipes&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.moeking.me%3A6969%2Fannounce&tr=udp%3A%2F%2Fopentor.org%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce"
link = "magnet:?xt=urn:btih:143D110F594868BF61A36E83880698589271999A&dn=You.Wont.Be.Alone.2022.MACEDONIAN.720p.WEBRip.800MB.x264-GalaxyRG&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.birkenwald.de%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.moeking.me%3A6969%2Fannounce&tr=udp%3A%2F%2Fopentor.org%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2970%2Fannounce&tr=https%3A%2F%2Ftracker.foreverpirates.co%3A443%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce"
handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()


def add_suffix(val):
    prefix = ['B', 'kB', 'MB', 'GB', 'TB']
    for i in range(len(prefix)):
        if abs(val) < 1000:
            if i == 0:
                return '%5.3g%s' % (val, prefix[i])
            else:
                return '%4.3g%s' % (val, prefix[i])
        val /= 1000

    return '%6.3gPB' % val




print('downloading metadata...')
while (not handle.has_metadata()):
    time.sleep(1)
print('got metadata, starting torrent download...')
while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
            'downloading', 'finished', 'seeding', 'allocating']
    # print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s') % \
    #         (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
    #         s.num_peers, state_stprint('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s') % \
    #         (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
    #         s.num_peers, state_str[s.state])
    os.system("clear||cls")
    progressw = (s.progress)
    downloadrt = (s.download_rate)
    uploadrt = (s.upload_rate)
    numpeers = (s.num_peers)
    print(s.state)
    xf = add_suffix(val=downloadrt)
    print("-----------------------")
    print(f"progress = {progressw}")
    print(f"upload = {uploadrt}")
    print(f"peers = {numpeers}")
    print(xf)
    # print(state_str)
    time.sleep(1)
