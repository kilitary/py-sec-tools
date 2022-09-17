rule __VMProtect_v1_25___PolyTech_sbrotl
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585A585E5D5B5B9D595FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
