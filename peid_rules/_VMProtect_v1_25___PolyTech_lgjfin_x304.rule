rule __VMProtect_v1_25___PolyTech_lgjfin
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585B5E5A585F58599D5DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
