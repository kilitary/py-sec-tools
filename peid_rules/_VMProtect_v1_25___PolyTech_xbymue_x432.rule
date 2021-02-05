rule __VMProtect_v1_25___PolyTech_xbymue
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A9D5E5A585F5D5B595FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
