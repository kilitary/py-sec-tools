rule __VMProtect_v1_25___PolyTech_ppjbzv
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5E9D5A5D5F585B595BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
