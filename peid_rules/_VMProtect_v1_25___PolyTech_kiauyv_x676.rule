rule __VMProtect_v1_25___PolyTech_kiauyv
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5253505551569C555768000000008B74242C89E581ECC000000089E70375008A0683C6010FB6C08D0C85????????FF218B6D00E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
