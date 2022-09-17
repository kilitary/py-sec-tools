rule _FASM_v1_3x_clflks
{
	meta:
		description = "FASM v1_3x"
	strings:
		$a = {6A??FF15????????A3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
