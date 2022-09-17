rule __VMProtect_v1_25___PolyTech_wbxlao
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8A068D7601668B550083C502881407E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
