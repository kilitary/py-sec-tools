rule __VMProtect_v1_25___PolyTech_nrmkby
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585E5A5F58585D595B9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
