import ctypes as ct
from ctypes import wintypes as w

PSID = w.LPVOID

kb = ct.WinDLL('kernelbase')  # documented as kernel32.dll but found in kernelbase.dll instead.
kb.DeriveCapabilitySidsFromName.argtypes = w.LPCWSTR, ct.POINTER(ct.POINTER(PSID)), ct.POINTER(w.DWORD), ct.POINTER(ct.POINTER(PSID)), ct.POINTER(w.DWORD)
kb.DeriveCapabilitySidsFromName.restype = w.BOOL

WELL_KNOWN_SID_TYPE = w.DWORD

kb.IsWellKnownSid.argtypes = ct.POINTER(PSID), WELL_KNOWN_SID_TYPE
kb.IsWellKnownSid.restype = w.BOOL

k32 = ct.WinDLL('kernel32')
k32.LocalFree.argtypes = w.HLOCAL,
k32.LocalFree.restype = w.HLOCAL
#
cap_name = ct.create_unicode_buffer(u'S-1-5-32-568')

cap_group_sids = ct.POINTER(PSID)()
cap_group_sid_count = w.DWORD()
cap_sids = ct.POINTER(PSID)()
cap_sid_count = w.DWORD()

result = kb.DeriveCapabilitySidsFromName(cap_name, ct.byref(cap_group_sids), ct.byref(cap_group_sid_count),
                                         ct.byref(cap_sids), ct.byref(cap_sid_count))
if result:
    print(f'sids groups {cap_group_sid_count.value} {cap_group_sids}:\r\n\t', cap_group_sids[:cap_group_sid_count.value], ' ', hex(cap_group_sids[0]))
    print(f'sids {cap_sid_count.value} {cap_sids}:\r\n\t', cap_sids[:cap_sid_count.value], ' ', hex(cap_sids[0]))
    
    for sid_known in range(0, 119):
        result = kb.IsWellKnownSid(cap_group_sids, sid_known)
        print(f'{(cap_group_sids[0])} IsWellKnown {sid_known}  => {result}')
    
    # These all print 'None' if free succeeds.
    for h in cap_group_sids[:cap_group_sid_count.value]:
        print(k32.LocalFree(h))
    for h in cap_sids[:cap_sid_count.value]:
        print(k32.LocalFree(h))
    print(k32.LocalFree(cap_group_sids))
    print(k32.LocalFree(cap_sids))
