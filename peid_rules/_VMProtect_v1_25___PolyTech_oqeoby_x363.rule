rule __VMProtect_v1_25___PolyTech_oqeoby
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595E585A5D5F5B5A599DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
