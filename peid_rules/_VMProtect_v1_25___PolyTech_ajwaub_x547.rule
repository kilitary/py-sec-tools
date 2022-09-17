rule __VMProtect_v1_25___PolyTech_ajwaub
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5057525351559C525668000000008B74242C89E581ECC000000089E70375008A06460FB6C0FF2485????????8B550083C5028A0266894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
