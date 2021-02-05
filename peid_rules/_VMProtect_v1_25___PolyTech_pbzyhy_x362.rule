rule __VMProtect_v1_25___PolyTech_pbzyhy
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595D5F5E5B9D585B595AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
