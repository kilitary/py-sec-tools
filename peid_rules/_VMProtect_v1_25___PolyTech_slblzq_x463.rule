rule __VMProtect_v1_25___PolyTech_slblzq
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5E595A5B9D5F58585DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
