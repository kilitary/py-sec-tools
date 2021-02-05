rule __VMProtect_v1_25___PolyTech_knysrw
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5A5B5F585D5E5D599DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
