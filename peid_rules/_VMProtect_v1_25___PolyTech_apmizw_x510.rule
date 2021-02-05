rule __VMProtect_v1_25___PolyTech_apmizw
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????52575651509C55575368000000008B74242C89E581ECC000000089E70375008A060FB6C083C6018D0C85????????FF2189E883ED0266894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
