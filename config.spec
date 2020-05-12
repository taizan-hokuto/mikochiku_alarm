# -*- mode: python ; coding: utf-8 -*-

def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                print('-----------',d)
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        print('-----------',f)
        extra_datas.append((f, f, 'DATA'))

    return extra_datas

block_cipher = None


a = Analysis(['mikochiku_alarm.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas += [('icon.ico','icon.ico','DATA')]
a.datas += [('alarm.mp3','alarm.mp3','DATA')]

'''
libmpg123.dll is called by pygame library and 
must be located directly under the root directory
or __MEIPASS (the Temporary dir while executing scripts).
'''
a.datas += [('libmpg123.dll','libmpg123.dll','DATA')]

# files under directory must be decompressed separately.
a.datas += extra_datas('lang')
a.datas += extra_datas('channel')
a.datas += extra_datas('css')
a.datas += extra_datas('img')

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='mikochiku_alarm',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,icon="icon.ico" )
