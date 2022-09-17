rule __VMProtect_v1_25___PolyTech_udjojt
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585A5B595D5E585F9D5DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
