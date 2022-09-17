rule __VMProtect_v1_25___PolyTech_agutgs
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????80E03C8B140783ED04895500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
