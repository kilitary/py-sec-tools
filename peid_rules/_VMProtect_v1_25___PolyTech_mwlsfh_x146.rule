rule __VMProtect_v1_25___PolyTech_mwlsfh
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????660FB70683ED0283C60266894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
