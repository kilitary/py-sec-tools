rule __VMProtect_v1_25___PolyTech_zucofr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585E5B5D5A5F5859589DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
