import sys

from cx_Freeze import setup, Executable

build_exe_options = {'include_files': ['ui_qry_song.pro', 'crazyktv.db3']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable = Executable('ui_qry_song.py', base=base)

setup(
        name = "qry_song",
        version = "0.2",
        description = "Check Image",
        options = {'build_exe': build_exe_options},
        executables = [executable])
