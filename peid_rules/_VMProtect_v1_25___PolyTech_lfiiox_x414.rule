rule __VMProtect_v1_25___PolyTech_lfiiox
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5D5E585A9D5F595B59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
