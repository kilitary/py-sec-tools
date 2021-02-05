rule __VMProtect_v1_25___PolyTech_nvachn
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC59585F5E595E5D5B5A9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
