rule __VMProtect_v1_25___PolyTech_dkxiro
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58589D5B5D5E5F5A595EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
