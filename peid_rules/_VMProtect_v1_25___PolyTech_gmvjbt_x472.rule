rule __VMProtect_v1_25___PolyTech_gmvjbt
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5F9D585B5D5A5A5E59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
