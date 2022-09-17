rule __VMProtect_v1_25___PolyTech_rkqjpm
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595D5F59595A5E5B9D58C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
