rule __VMProtect_v1_25___PolyTech_uqcxhm
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A585F5E5E5A5D5B599DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
