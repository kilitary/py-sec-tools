rule _DxPack_V0_86__Dxd_qadasg
{
	meta:
		description = "DxPack V0_86 __ Dxd"
	strings:
		$a = {54E8????????5D8BC581ED7144????2B856460????EB43DF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
