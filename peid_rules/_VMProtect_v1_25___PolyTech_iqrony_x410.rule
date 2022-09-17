rule __VMProtect_v1_25___PolyTech_iqrony
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5B5D5F5E9D585A5958C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
