rule __VMProtect_v1_25___PolyTech_mymqyd
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8B0683EEFC83ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
