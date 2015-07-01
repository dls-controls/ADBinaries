import xml.dom.minidom
from iocbuilder import Substitution, AutoSubstitution, SetSimulation, Device, records, Architecture, IocDataStream
from iocbuilder.arginfo import *

__all__ = ['ADBinaries']

#############################
#    ADBinary base class    #
#############################

class ADBinaries(Device):
    """Library dependencies for ADBinaries"""
    if Architecture() == "win32-x86" or Architecture() == "windows-x64":
        # Temporarily set this to false as 64bit not working with DLS
        usemagic = False
        if Architecture() == "win32-x86":
            # The Magic libraries for 32bit do not work with the DLS toolchain
            # MSVC2010. So we cant use them.
            usemagic = False
        usehdfdlls = True
        hdfdlls = ['zlib', 'szip', 'hdf5', 'libxml2']
        hdfstatic = ['zlib', 'libszip', 'hdf5', 'libxml2']
        magiclibs = ['CORE_RL_zlib_',
            'CORE_RL_xlib_', 'CORE_RL_wmf_', 'CORE_RL_ttf_', 'CORE_RL_tiff_',
            'CORE_RL_png_', 'CORE_RL_libxml_', 'CORE_RL_lcms_', 'CORE_RL_jpeg_',
            'CORE_RL_jp2_', 'CORE_RL_jbig_', 'CORE_RL_bzlib_',
            'CORE_RL_filters_', 'CORE_RL_coders_', 'CORE_RL_magick_',
            'CORE_RL_wand_', 'CORE_RL_Magick++_']
        LibFileList = ['NeXus'] #, 'PvAPI']
        if usemagic:
            LibFileList += magiclibs
        else:
            LibFileList += ['jpeg', 'tiff']
        if usehdfdlls:
            LibFileList = hdfdlls + LibFileList
        else:
            LibFileList = hdfstatic + LibFileList
        SysLibFileList = ['Oleaut32', 'Gdi32']

    AutoInstantiate = True

#############################

