rule __VMProtect_v1_25___PolyTech_skykkg
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????515253559C5556575068000000008B74242C89E581ECC000000089E70375008A060FB6C08D7601FF2485????????89E883ED0266894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
