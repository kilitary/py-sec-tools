rule __VMProtect_v1_25___PolyTech_anuycd
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC599D5B5D5A5F595E5859C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
