rule __VMProtect_v1_25___PolyTech_wxwvfv
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5A5F5D9D5859595B5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
