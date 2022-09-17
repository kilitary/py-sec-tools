rule __VMProtect_v1_25___PolyTech_sxtbdv
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????55575056515253509C68000000008B74242C89E581ECC000000089E70375008A060FB6C046FF2485????????8B45008A550483C5068810E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
