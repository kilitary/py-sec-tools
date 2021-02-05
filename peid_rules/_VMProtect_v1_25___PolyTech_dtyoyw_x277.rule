rule __VMProtect_v1_25___PolyTech_dtyoyw
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58585F5B5F5D595E9D5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
