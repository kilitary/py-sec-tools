rule __VMProtect_v1_25___PolyTech_gbwevg
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????0FB606468A040783ED0266894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
