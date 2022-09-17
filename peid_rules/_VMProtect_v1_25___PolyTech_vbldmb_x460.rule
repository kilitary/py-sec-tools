rule __VMProtect_v1_25___PolyTech_vbldmb
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5E585D5A5A5F5B9D59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
