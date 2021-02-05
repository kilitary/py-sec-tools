rule _MASM_TASM_qrszzv
{
	meta:
		description = "MASM  TASM"
	strings:
		$a = {6A00E8????0000A3??324000E8????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
