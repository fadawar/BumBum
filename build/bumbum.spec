# -*- mode: python -*-

block_cipher = None


a = Analysis(['../bumbum/bumbum.py'],
             pathex=['/Users/jozefg/PycharmProjects/BumBum/build'],
             binaries=[],
             datas=[('../bumbum/gui', 'gui')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['_md5', '_sha1', '_sha256', '_sha512'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='bumbum',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='bumbum')
app = BUNDLE(coll,
             name='bumbum.app',
             icon=None,
             bundle_identifier=None)
