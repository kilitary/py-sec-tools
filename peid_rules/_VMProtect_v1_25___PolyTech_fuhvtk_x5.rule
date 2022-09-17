rule __VMProtect_v1_25___PolyTech_fuhvtk
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????668B45008A4D0283ED0266D3E8668945049C8F4500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
