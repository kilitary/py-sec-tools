rule __VMProtect_v1_25___PolyTech_mwiuox
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5959585A5F5B5E5D5D9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
