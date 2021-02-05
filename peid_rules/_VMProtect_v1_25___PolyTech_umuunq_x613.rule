rule __VMProtect_v1_25___PolyTech_umuunq
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????509C5357525756515568000000008B74242C89E581ECC000000089E70375008A060FB6C083C601FF2485????????8B45008B00894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
