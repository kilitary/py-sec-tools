rule _AHPack_0_1__FEUERRADER_nthdtq
{
	meta:
		description = "AHPack 0_1 __ FEUERRADER"
	strings:
		$a = {606854????00B848????00FF1068B3????0050B844????00FF106800}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
