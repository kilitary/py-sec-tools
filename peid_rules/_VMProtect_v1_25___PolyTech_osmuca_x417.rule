rule __VMProtect_v1_25___PolyTech_osmuca
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5D5F5B5D585E5A599DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
