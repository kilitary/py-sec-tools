rule __VMProtect_v1_25___PolyTech_xyosol
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585F5A5E5E599D5D5B58C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
