rule __VMProtect_v1_25___PolyTech_bynjzv
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5A5B5A5F5E5D5858599DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
