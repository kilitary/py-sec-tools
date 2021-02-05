rule __VMProtect_v1_25___PolyTech_xsdtfa
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5858595E5D5B9D5F5A5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
