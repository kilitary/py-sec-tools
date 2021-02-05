rule __VMProtect_v1_25___PolyTech_idyhbt
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5A585B595E5D5F5F9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
