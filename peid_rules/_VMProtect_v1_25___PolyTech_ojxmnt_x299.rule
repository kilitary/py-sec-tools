rule __VMProtect_v1_25___PolyTech_ojxmnt
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585A9D5E5B5F5B585D59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
