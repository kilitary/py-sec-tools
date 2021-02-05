rule __VMProtect_v1_25___PolyTech_gmyguv
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????660FB7069883ED0489450083C602E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
