rule __VMProtect_v1_25___PolyTech_uxwqdw
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC59595D58599D5E5A5B5FC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
