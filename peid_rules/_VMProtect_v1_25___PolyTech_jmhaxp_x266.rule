rule __VMProtect_v1_25___PolyTech_jmhaxp
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8B45008B550483C5088910E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
