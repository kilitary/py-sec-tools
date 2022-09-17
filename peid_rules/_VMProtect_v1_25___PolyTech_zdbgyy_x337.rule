rule __VMProtect_v1_25___PolyTech_zdbgyy
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC59585B5A5F595D5D5E9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
