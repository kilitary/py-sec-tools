rule __VMProtect_v1_25___PolyTech_fcmrdm
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585F5E5D599D5B585A5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
