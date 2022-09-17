rule __VMProtect_v1_25___PolyTech_jzqork
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????0FB60683ED026689450083C601E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
