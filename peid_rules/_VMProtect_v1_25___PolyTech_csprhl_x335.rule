rule __VMProtect_v1_25___PolyTech_csprhl
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC59585B59595E5D5F5A9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
