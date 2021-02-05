rule __VMProtect_v1_25___PolyTech_fwxwox
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585F5E585D5B599D5A5DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
