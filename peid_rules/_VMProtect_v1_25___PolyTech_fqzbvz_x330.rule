rule __VMProtect_v1_25___PolyTech_fqzbvz
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC589D585F5F5B5A595D5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
