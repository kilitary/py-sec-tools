rule __VMProtect_v1_25___PolyTech_ybyfwi
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585F5B5E5B5D595A9D58C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
