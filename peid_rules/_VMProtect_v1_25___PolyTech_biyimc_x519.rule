rule __VMProtect_v1_25___PolyTech_biyimc
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????555657515253539C5068000000008B74242C89E581ECC000000089E70375008A060FB6C0468D0C85????????FF218B45008A550483C5068810E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
