rule __VMProtect_v1_25___PolyTech_cxjckv
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????0FB6068A040783EEFF83ED0266894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
