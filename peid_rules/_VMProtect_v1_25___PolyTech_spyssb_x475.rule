rule __VMProtect_v1_25___PolyTech_spyssb
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B9D5D5E595B585B5F5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
