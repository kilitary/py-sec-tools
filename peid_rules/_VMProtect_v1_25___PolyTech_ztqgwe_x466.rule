rule __VMProtect_v1_25___PolyTech_ztqgwe
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5E5D5B5A9D585A595FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
