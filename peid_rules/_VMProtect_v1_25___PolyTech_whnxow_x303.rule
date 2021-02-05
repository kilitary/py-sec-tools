rule __VMProtect_v1_25___PolyTech_whnxow
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585B5D5E595F589D585AC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
