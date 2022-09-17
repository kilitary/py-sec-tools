rule __VMProtect_v1_25___PolyTech_dgcgcc
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC599D5A585B5F595D5E59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
