rule _MASM_TASM_nbupyn
{
	meta:
		description = "MASM  TASM"
	strings:
		$a = {535152565755E8????????5D81ED423040??FF95323540??B8373040??03C52B851B3440??8985273440??83}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
