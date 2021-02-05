rule __VMProtect_v1_25___PolyTech_slrntp
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC59585B9D5A5F5D5A5E59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
