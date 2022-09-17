rule __VMProtect_v1_25___PolyTech_scrmzz
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5F59595A5B9D5E585DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
