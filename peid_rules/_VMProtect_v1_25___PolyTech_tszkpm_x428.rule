rule __VMProtect_v1_25___PolyTech_tszkpm
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5F5A595D9D5E585B5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
