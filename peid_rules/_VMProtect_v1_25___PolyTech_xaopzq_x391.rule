rule __VMProtect_v1_25___PolyTech_xaopzq
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A585E5F5D5A585B9D59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
