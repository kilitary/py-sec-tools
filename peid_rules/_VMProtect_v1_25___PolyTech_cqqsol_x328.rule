rule __VMProtect_v1_25___PolyTech_cqqsol
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585F5E9D5D585B5A5A59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
