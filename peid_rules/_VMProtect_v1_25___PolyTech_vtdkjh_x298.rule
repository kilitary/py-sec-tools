rule __VMProtect_v1_25___PolyTech_vtdkjh
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585A9D5E595D5D585B5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
