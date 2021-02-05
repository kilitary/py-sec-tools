rule __VMProtect_v1_25___PolyTech_gyeziu
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585D5E9D5F5B5A5B5859C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
