rule __VMProtect_v1_25___PolyTech_qfowij
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5B9D5859585E5D5A5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
