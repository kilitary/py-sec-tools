rule __VMProtect_v1_25___PolyTech_nqzoep
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A58595E9D5F595A5B5DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
