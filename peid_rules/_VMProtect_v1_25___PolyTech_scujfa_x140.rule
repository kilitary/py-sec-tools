rule __VMProtect_v1_25___PolyTech_scujfa
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????0FB6068A040783ED026689450046E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
