rule __VMProtect_v1_25___PolyTech_ctyaik
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????509C5653535557525168000000008B74242C89E581ECC000000089E70375008A060FB6C046FF2485????????8B45000145049C8F4500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
