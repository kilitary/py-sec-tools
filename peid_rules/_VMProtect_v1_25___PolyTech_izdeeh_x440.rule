rule __VMProtect_v1_25___PolyTech_izdeeh
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B595E5A5F5B9D5B585DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
