rule __VMProtect_v1_25___PolyTech_wcewij
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5650529C525157535568000000008B74242C89E581ECC000000089E70375008A06460FB6C0FF2485????????8B45008B550483C508368910E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
