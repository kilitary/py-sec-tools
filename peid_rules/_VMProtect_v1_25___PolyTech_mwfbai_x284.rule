rule __VMProtect_v1_25___PolyTech_mwfbai
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC58595B9D5E5F5A585D5DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
