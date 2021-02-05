rule __VMProtect_v1_25___PolyTech_ltkyxp
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????0FB60666989883ED0489450046E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
