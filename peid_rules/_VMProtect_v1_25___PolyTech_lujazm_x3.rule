rule __VMProtect_v1_25___PolyTech_lujazm
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8B45008B55048A4D0883C5020FADD08945049C8F4500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
