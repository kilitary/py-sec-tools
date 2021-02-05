rule __VMProtect_v1_25___PolyTech_nzakxp
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????539C5250515756555568000000008B74242C89E581ECC000000089E70375008A0683EEFF0FB6C0FF2485????????8B45008B00894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
