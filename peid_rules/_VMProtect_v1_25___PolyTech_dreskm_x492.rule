rule __VMProtect_v1_25___PolyTech_dreskm
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5053509C515752555668000000008B74242C89E581ECC000000089E70375008A06460FB6C08D0C85????????FF218B0683EEFC83ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
