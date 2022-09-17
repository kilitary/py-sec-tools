rule _PE_Lock_NT_v2_04_txqmoh
{
	meta:
		description = "PE Lock NT v2_04"
	strings:
		$a = {EB????BE????BF????2E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
