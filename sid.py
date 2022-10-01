import ctypes as ct
from ctypes import wintypes as w

PSID = w.LPVOID

kb = ct.WinDLL('kernelbase') # documented as kernel32.dll but found in kernelbase.dll instead.
kb.DeriveCapabilitySidsFromName.argtypes = w.LPCWSTR, ct.POINTER(ct.POINTER(PSID)), ct.POINTER(w.DWORD), ct.POINTER(ct.POINTER(PSID)), ct.POINTER(w.DWORD)
kb.DeriveCapabilitySidsFromName.restype = w.BOOL

k32 = ct.WinDLL('kernel32')
k32.LocalFree.argtypes = w.HLOCAL,
k32.LocalFree.restype = w.HLOCAL

cap_name = ct.create_unicode_buffer('S-1-15-3-1024-3424233489-972189580-2057154623-747635277-1604371224-316187997-3786583170-1043257646')

cap_group_sids = ct.POINTER(PSID)()
cap_group_sid_count = w.DWORD()
cap_sids = ct.POINTER(PSID)()
cap_sid_count = w.DWORD()

result = kb.DeriveCapabilitySidsFromName(cap_name, ct.byref(cap_group_sids), ct.byref(cap_group_sid_count),
                                          ct.byref(cap_sids), ct.byref(cap_sid_count))
if result:
    print(cap_group_sid_count.value)
    print(cap_group_sids[:cap_group_sid_count.value])
    print(cap_sid_count.value)
    print(cap_sids[:cap_sid_count.value])

    # These all print 'None' if free succeeds.
    for h in cap_group_sids[:cap_group_sid_count.value]:
        print(k32.LocalFree(h))
    for h in cap_sids[:cap_sid_count.value]:
        print(k32.LocalFree(h))
    print(k32.LocalFree(cap_group_sids))
    print(k32.LocalFree(cap_sids))
