rule __VMProtect_v1_25___PolyTech_bxzhsm
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58595D5F5E5A5B9D5B58C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
