rule __VMProtect_v1_25___PolyTech_mmvlik
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5959585B5E5F5A9D5DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
