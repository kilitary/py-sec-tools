rule _MASM_TASM_zaiibw
{
	meta:
		description = "MASM  TASM"
	strings:
		$a = {6A00E8??0?0000A3??324000E8??0?0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
