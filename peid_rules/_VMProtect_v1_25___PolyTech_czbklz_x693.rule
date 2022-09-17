rule __VMProtect_v1_25___PolyTech_czbklz
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????505651519C5255575368000000008B74242C89E581ECC000000089E70375008A060FB6C083C601FF2485????????8B6D00E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
