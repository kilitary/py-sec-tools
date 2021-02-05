rule __VMProtect_v1_25___PolyTech_lnkyuo
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58595E585D5B9D5F5A5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
