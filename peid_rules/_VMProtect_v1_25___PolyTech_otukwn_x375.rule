rule __VMProtect_v1_25___PolyTech_otukwn
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595F5D58599D5E5B5A5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
