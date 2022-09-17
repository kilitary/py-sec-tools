rule __VMProtect_v1_25___PolyTech_kqdnsl
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585D5E5B5F585E595A9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
