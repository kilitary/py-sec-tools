rule __VMProtect_v1_25___PolyTech_gyksyp
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????50535157539C52555668000000008B74242C89E581ECC000000089E70375008A0683C6010FB6C08D0C85????????FF218B4500368B00894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
