rule __VMProtect_v1_25___PolyTech_hmhojj
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5E5F58599D5F5B5D5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
