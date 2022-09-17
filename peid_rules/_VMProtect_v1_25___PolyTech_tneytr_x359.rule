rule __VMProtect_v1_25___PolyTech_tneytr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595D5E9D585B5F59585AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
