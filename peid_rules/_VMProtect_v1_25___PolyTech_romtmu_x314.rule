rule __VMProtect_v1_25___PolyTech_romtmu
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585D5F5E589D595A5B5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
