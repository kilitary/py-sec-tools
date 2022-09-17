rule __VMProtect_v1_25___PolyTech_qyuyzr
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC59585B595F5A5E5D9D5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
