rule __VMProtect_v1_25___PolyTech_iyvala
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????660FB7069883ED0489450083EEFEE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
