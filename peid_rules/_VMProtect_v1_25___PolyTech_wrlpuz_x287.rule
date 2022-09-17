rule __VMProtect_v1_25___PolyTech_wrlpuz
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58595E5B5F5B9D585D5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
