rule __VMProtect_v1_25___PolyTech_jiqalw
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5D5E585F5A595B5B9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
