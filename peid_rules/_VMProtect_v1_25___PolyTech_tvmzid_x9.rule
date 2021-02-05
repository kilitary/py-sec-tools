rule __VMProtect_v1_25___PolyTech_tvmzid
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8B45008B5504F7D0F7D221D08945049C8F4500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
