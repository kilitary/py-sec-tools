rule __VMProtect_v1_25___PolyTech_qnscze
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????0FB606668B040783ED02668945008D7601E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
