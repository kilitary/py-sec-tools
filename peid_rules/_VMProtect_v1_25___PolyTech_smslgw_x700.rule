rule __VMProtect_v1_25___PolyTech_smslgw
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5655539C575251555068000000008B74242C89E581ECC000000089E70375008A060FB6C046FF2485????????668B6D00E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
