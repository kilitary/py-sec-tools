rule __VMProtect_v1_25___PolyTech_auurie
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????559C5253505151575668000000008B74242C89E581ECC000000089E70375008A060FB6C046FF3485????????C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
