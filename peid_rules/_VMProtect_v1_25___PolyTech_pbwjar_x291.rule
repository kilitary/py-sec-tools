rule __VMProtect_v1_25___PolyTech_pbwjar
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585A595B5D5A5E9D5F58C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
