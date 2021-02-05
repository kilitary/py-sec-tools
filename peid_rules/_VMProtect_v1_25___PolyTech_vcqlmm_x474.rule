rule __VMProtect_v1_25___PolyTech_vcqlmm
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B9D5D59585F5A5E5B5BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
