rule __VMProtect_v1_25___PolyTech_pxwadz
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B585A5E5F5B5B5D599DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
