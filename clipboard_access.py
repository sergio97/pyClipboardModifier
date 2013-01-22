import ctypes

#Get required functions, strcpy..
strcpy = ctypes.cdll.msvcrt.strcpy
ocb = ctypes.windll.user32.OpenClipboard        #Basic Clipboard functions
ecb = ctypes.windll.user32.EmptyClipboard
gcd = ctypes.windll.user32.GetClipboardData
scd = ctypes.windll.user32.SetClipboardData
ccb = ctypes.windll.user32.CloseClipboard
ga = ctypes.windll.kernel32.GlobalAlloc     # Global Memory allocation
gl = ctypes.windll.kernel32.GlobalLock       # Global Memory Locking
gul = ctypes.windll.kernel32.GlobalUnlock
GMEM_DDESHARE = 0x2000 

def Get( ):
    ocb(None) # Open Clip, Default task
    pcontents = gcd(1) # 1 means CF_TEXT.. too lazy to get the token thingy ... 
    data = ctypes.c_char_p(pcontents).value
    #gul(pcontents) ?
    ccb()
    return bytes.decode(data)

def Paste( data ):
    ocb(None) # Open Clip, Default task
    ecb()
    hCd = ga( GMEM_DDESHARE, len( str.encode(data) )+1 )
    pchData = gl(hCd)
    strcpy(ctypes.c_char_p(pchData),str.encode(data))
    gul(hCd)
    scd(1,hCd)
    ccb()