# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['unit_converter.py'],
    pathex=[],
    binaries=[('C:\\Users\\maxim\\AppData\\Local\\spyder-6\\Library\\bin\\tk86t.dll', '.'), ('C:\\Users\\maxim\\AppData\\Local\\spyder-6\\Library\\bin\\tcl86t.dll', '.')],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='unit_converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
