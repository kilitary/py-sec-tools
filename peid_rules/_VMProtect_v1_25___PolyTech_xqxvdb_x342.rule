rule __VMProtect_v1_25___PolyTech_xqxvdb
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC59589D5F5D5E5B595A5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
