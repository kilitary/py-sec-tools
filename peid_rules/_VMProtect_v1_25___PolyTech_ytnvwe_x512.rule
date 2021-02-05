rule __VMProtect_v1_25___PolyTech_ytnvwe
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5352569C575051555068000000008B74242C89E581ECC000000089E70375008A06460FB6C08D0C85????????FF218B45008B550483C5088910E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
