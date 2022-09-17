rule __VMProtect_v1_25___PolyTech_ebikqj
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5E5D5B5F5E59589D5AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
